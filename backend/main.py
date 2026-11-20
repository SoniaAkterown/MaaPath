import os
import random
from typing import Dict, Optional
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import init_db, get_db, Mother, VitalLog, ANCVisit, Referral
from agents import maapath_workflow

app = FastAPI(title="MaaPath AI Clinical Backend", version="1.0.0")

# ফ্রন্টএন্ড (HTML) থেকে কল করার জন্য CORS চালু
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()


# ---------- Pydantic Schemas ----------
class MotherCreate(BaseModel):
    name: str
    age: int
    phone: str
    guardian_phone: Optional[str] = ""
    address: str
    lmp: str
    blood_group: str = "O+"
    prev_history: str = "First Pregnancy"
    bp: str = "118/76"
    weight: str = "58.5 kg"
    diseases: str = "None"
    medications: str = "Iron-Folic Acid (IFA), Calcium 500mg"


class VitalCreate(BaseModel):
    mother_id: str
    date: str = "18 Nov 2026"
    week: str = "24w"
    bp: str
    weight: str
    sugar: str = "5.4 mmol/L"
    hb: str = "11.8 g/dL"


class RiskScreenRequest(BaseModel):
    mother_id: Optional[str] = None
    danger_signs: Dict[str, bool]
    bp: Optional[str] = "120/80"


class ChatRequest(BaseModel):
    question: str
    lang: str = "bn"


class ReferralCreate(BaseModel):
    mother_id: str
    hospital_name: str
    urgency: str = "High"
    reason: str = "Clinical escalation via MaaPath AI"


# ---------- Serve Frontend Index ----------
FRONTEND_INDEX = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
)

@app.get("/")
def serve_frontend():
    if os.path.exists(FRONTEND_INDEX):
        return FileResponse(FRONTEND_INDEX)
    return {"message": "MaaPath AI API is running. Put index.html inside ../frontend/"}


# ---------- API Endpoints ----------
@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "MaaPath AI Multi-Agent Clinical API"}


@app.post("/api/mothers")
def register_mother(payload: MotherCreate, db: Session = Depends(get_db)):
    # LangGraph Intake + ANC Planning Agent রান
    result = maapath_workflow.invoke({"task": "intake", "lmp": payload.lmp})
    mother_id = f"MP-BD-{random.randint(2500, 9999)}"

    mother = Mother(
        id=mother_id,
        name=payload.name,
        age=payload.age,
        phone=payload.phone,
        guardian_phone=payload.guardian_phone,
        address=payload.address,
        lmp=payload.lmp,
        edd=result["edd"],
        pregnancy_week=result["gestational_week"],
        blood_group=payload.blood_group,
        prev_history=payload.prev_history,
        diseases=payload.diseases,
        medications=payload.medications,
        risk_level="Moderate" if payload.diseases.lower() not in ["none", ""] else "Low",
    )
    db.add(mother)

    # প্রথম বেসলাইন ভাইটাল লগ
    db.add(VitalLog(
        mother_id=mother_id,
        date="18 Nov 2026",
        week=f"{result['gestational_week']}w",
        bp=payload.bp,
        weight=payload.weight,
    ))

    # অটো-জেনারেটেড ANC ভিজিটগুলো সেভ
    for v in result.get("anc_schedule", []):
        db.add(ANCVisit(mother_id=mother_id, **v))

    db.commit()
    db.refresh(mother)
    return {
        "mother_id": mother.id,
        "name": mother.name,
        "edd": mother.edd,
        "gestational_week": mother.pregnancy_week,
        "trimester": result["trimester"],
        "anc_count": len(result.get("anc_schedule", [])),
        "agents_executed": result.get("agents_executed", []),
    }


@app.get("/api/mothers")
def list_mothers(db: Session = Depends(get_db)):
    mothers = db.query(Mother).order_by(Mother.created_at.desc()).all()
    return mothers


@app.post("/api/vitals")
def add_vital(payload: VitalCreate, db: Session = Depends(get_db)):
    vital = VitalLog(**payload.model_dump())
    db.add(vital)
    db.commit()
    db.refresh(vital)
    return {"status": "saved", "id": vital.id}


@app.post("/api/risk-screen")
def run_risk_screen(payload: RiskScreenRequest):
    result = maapath_workflow.invoke({
        "task": "risk_screen",
        "danger_signs": payload.danger_signs,
        "bp": payload.bp or "120/80",
    })
    return {
        "risk_level": result["risk_level"],
        "active_danger_count": result["active_danger_count"],
        "emergency": result["emergency"],
        "recommended_hospital": result.get("recommended_hospital"),
        "agents_executed": result.get("agents_executed", []),
    }


@app.post("/api/chat")
def clinical_chat(payload: ChatRequest):
    result = maapath_workflow.invoke({
        "task": "chat",
        "question": payload.question,
        "lang": payload.lang,
    })
    return {
        "reply": result["rag_answer"],
        "citation": result["rag_citation"],
        "emergency": result["emergency"],
        "recommended_hospital": result.get("recommended_hospital"),
        "agents_executed": result.get("agents_executed", []),
    }


@app.post("/api/referrals")
def create_referral(payload: ReferralCreate, db: Session = Depends(get_db)):
    ref = Referral(**payload.model_dump())
    db.add(ref)
    db.commit()
    db.refresh(ref)
    return {"status": "Dispatched & Notified", "referral_id": ref.id}
