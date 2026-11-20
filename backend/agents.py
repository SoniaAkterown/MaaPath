from datetime import datetime, timedelta
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, END
from clinical_rag import query_clinical_rag


class MaaPathState(TypedDict, total=False):
    task: str                        # "intake" | "risk_screen" | "chat"
    lang: str                        # "en" | "bn"
    lmp: str                         # YYYY-MM-DD
    danger_signs: Dict[str, bool]
    bp: str
    question: str
    address: str
    # Outputs
    edd: str
    gestational_week: int
    trimester: str
    anc_schedule: List[Dict[str, str]]
    risk_level: str
    active_danger_count: int
    recommended_hospital: Optional[str]
    rag_answer: str
    rag_citation: str
    emergency: bool
    agents_executed: List[str]


def intake_agent(state: MaaPathState) -> MaaPathState:
    """LMP থেকে EDD, বর্তমান সপ্তাহ ও ট্রাইমেস্টার নির্ণয় করে"""
    lmp_str = state.get("lmp", "2026-06-03")
    lmp_dt = datetime.strptime(lmp_str, "%Y-%m-%d")
    edd_dt = lmp_dt + timedelta(days=280)
    today = datetime.now()
    weeks = max(1, min(42, (today - lmp_dt).days // 7))
    trimester = "Trimester 1" if weeks <= 12 else "Trimester 2" if weeks <= 27 else "Trimester 3"

    executed = state.get("agents_executed", []) + ["Intake Agent"]
    return {
        **state,
        "edd": edd_dt.strftime("%d %b %Y"),
        "gestational_week": weeks,
        "trimester": trimester,
        "agents_executed": executed,
    }


def anc_planning_agent(state: MaaPathState) -> MaaPathState:
    """WHO 8-Contact গাইডলাইন অনুযায়ী ANC চেকআপ শিডিউল তৈরি করে"""
    lmp_dt = datetime.strptime(state.get("lmp", "2026-06-03"), "%Y-%m-%d")
    contact_weeks = [12, 20, 26, 30, 34, 36, 38, 40]
    schedule = []
    for idx, wk in enumerate(contact_weeks, start=1):
        visit_dt = lmp_dt + timedelta(weeks=wk)
        schedule.append({
            "title": f"ANC Visit #{idx} (Week {wk})",
            "scheduled_date": visit_dt.strftime("%d %b %Y"),
            "location": "Savar Upazila Health Complex",
            "notes": "BP, Weight, Hemoglobin, Fetal Heart & Danger Sign Screening",
            "status": "completed" if wk < state.get("gestational_week", 1) else "upcoming"
        })

    executed = state.get("agents_executed", []) + ["ANC Planning Agent"]
    return {**state, "anc_schedule": schedule, "agents_executed": executed}


def risk_screening_agent(state: MaaPathState) -> MaaPathState:
    """৭টি বিপদচিহ্ন ও রক্তচাপ যাচাই করে ঝুঁকির মাত্রা নির্ণয় করে"""
    signs = state.get("danger_signs", {})
    active_count = sum(1 for v in signs.values() if v)
    high_bp = False

    bp = state.get("bp", "")
    if "/" in bp:
        try:
            sys_bp, dia_bp = [int(x.strip()) for x in bp.split("/")[:2]]
            if sys_bp >= 140 or dia_bp >= 90:
                high_bp = True
        except ValueError:
            pass

    if active_count >= 2 or signs.get("bleeding") or signs.get("convulsion") or high_bp:
        risk_level = "HIGH EMERGENCY RISK"
        emergency = True
    elif active_count == 1:
        risk_level = "Moderate Risk"
        emergency = True
    else:
        risk_level = "Low Risk"
        emergency = False

    executed = state.get("agents_executed", []) + ["Risk Screening Agent"]
    return {
        **state,
        "risk_level": risk_level,
        "active_danger_count": active_count,
        "emergency": emergency,
        "agents_executed": executed,
    }


def referral_agent(state: MaaPathState) -> MaaPathState:
    """উচ্চ ঝুঁকিপূর্ণ রোগীর জন্য নিকটস্থ হাসপাতাল নির্ধারণ করে"""
    hospital = None
    if state.get("emergency"):
        hospital = (
            "Dhaka Medical College & Hospital (NICU/EmOC)"
            if state.get("risk_level") == "HIGH EMERGENCY RISK"
            else "Savar Upazila Health Complex (24/7 Obs)"
        )
    executed = state.get("agents_executed", []) + ["Referral Agent"]
    return {**state, "recommended_hospital": hospital, "agents_executed": executed}


def clinical_rag_agent(state: MaaPathState) -> MaaPathState:
    """WHO & DGHS ক্লিনিক্যাল RAG থেকে উত্তর ও সাইটেশন আনে"""
    res = query_clinical_rag(state.get("question", ""), state.get("lang", "bn"))
    executed = state.get("agents_executed", []) + ["Clinical RAG Agent"]
    return {
        **state,
        "rag_answer": res["answer"],
        "rag_citation": res["citation"],
        "emergency": res["emergency"],
        "agents_executed": executed,
    }


def route_task(state: MaaPathState) -> str:
    task = state.get("task", "chat")
    if task == "intake":
        return "intake_agent"
    if task == "risk_screen":
        return "risk_screening_agent"
    return "clinical_rag_agent"


def build_maapath_graph():
    graph = StateGraph(MaaPathState)

    graph.add_node("intake_agent", intake_agent)
    graph.add_node("anc_planning_agent", anc_planning_agent)
    graph.add_node("risk_screening_agent", risk_screening_agent)
    graph.add_node("referral_agent", referral_agent)
    graph.add_node("clinical_rag_agent", clinical_rag_agent)

    graph.set_conditional_entry_point(
        route_task,
        {
            "intake_agent": "intake_agent",
            "risk_screening_agent": "risk_screening_agent",
            "clinical_rag_agent": "clinical_rag_agent",
        },
    )

    graph.add_edge("intake_agent", "anc_planning_agent")
    graph.add_edge("anc_planning_agent", END)

    graph.add_edge("risk_screening_agent", "referral_agent")
    graph.add_edge("referral_agent", END)

    graph.add_edge("clinical_rag_agent", "referral_agent")

    return graph.compile()


maapath_workflow = build_maapath_graph()
