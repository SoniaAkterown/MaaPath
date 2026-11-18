from typing import Dict, Any, List

# WHO ANC (2016) & DGHS Bangladesh Maternal Protocol ভেরিফাইড নলেজ বেস
CLINICAL_KB: List[Dict[str, Any]] = [
    {
        "id": "emoc_preeclampsia",
        "keywords": ["মাথা", "ঝাপসা", "রক্তচাপ", "খিঁচুনি", "headache", "vision", "blurred", "convulsion", "bp", "pressure", "pre-eclampsia"],
        "emergency": True,
        "reply_bn": "জরুরী সতর্কতা! তীব্র মাথাব্যথা, চোখে ঝাপসা দেখা, খিঁচুনি বা উচ্চ রক্তচাপ (≥140/90) প্রি-এক্লাম্পসিয়া বা এক্লাম্পসিয়ার বিপদচিহ্ন। দেরি না করে এখনই নিকটস্থ উপজেলা স্বাস্থ্য কমপ্লেক্স বা জেলা হাসপাতালে যান অথবা ৯৯৯-এ কল করুন।",
        "reply_en": "EMERGENCY ALERT! Severe headache, blurred vision, convulsions, or high blood pressure (≥140/90) are danger signs of Pre-eclampsia/Eclampsia. Go immediately to the nearest Upazila Health Complex or District Hospital, or call 999.",
        "citation": "WHO Emergency Obstetric Care (EmOC) • DGHS Bangladesh Pre-eclampsia Protocol"
    },
    {
        "id": "emoc_bleeding",
        "keywords": ["রক্ত", "রক্তক্ষরণ", "ব্লিডিং", "bleeding", "blood", "spotting", "hemorrhage"],
        "emergency": True,
        "reply_bn": "জরুরী সতর্কতা! গর্ভাবস্থায় যেকোনো ধরনের যোনিপথে রক্তক্ষরণ গুরুতর বিপদচিহ্ন। মাকে শান্ত রেখে সাথে সাথে নিকটস্থ ইমার্জেন্সি অবস্টেট্রিক কেয়ার (EmOC) হাসপাতালে নিয়ে যান।",
        "reply_en": "EMERGENCY ALERT! Any vaginal bleeding during pregnancy is a critical danger sign. Keep the mother calm and transport immediately to the nearest EmOC hospital.",
        "citation": "WHO Maternal Danger Signs Guideline • DGHS Bangladesh EmOC Protocol"
    },
    {
        "id": "emoc_fetal_movement",
        "keywords": ["নড়াচড়া", "বাচ্চা", "নড়ে না", "কম নড়ছে", "movement", "kick", "fetal", "baby not moving"],
        "emergency": True,
        "reply_bn": "জরুরী সতর্কতা! গর্ভস্থ শিশুর নড়াচড়া কমে যাওয়া বা বন্ধ হয়ে যাওয়া অত্যন্ত গুরুত্বপূর্ণ সতর্কতা। বাম কাত হয়ে শুয়ে ২ ঘণ্টায় অন্তত ১০ বার নড়াচড়া অনুভব না করলে দ্রুত ডাক্তারের কাছে যান।",
        "reply_en": "URGENT ALERT! Reduced or absent fetal movement requires immediate assessment. Lie on your left side; if you feel fewer than 10 movements in 2 hours, visit a doctor immediately.",
        "citation": "WHO ANC Contact Guidelines • DGHS Fetal Monitoring Protocol"
    },
    {
        "id": "supplements_ifa_calcium",
        "keywords": ["আয়রন", "ক্যালসিয়াম", "ট্যাবলেট", "ফলিক", "ওষুধ", "iron", "calcium", "folic", "ifa", "tablet", "supplement"],
        "emergency": False,
        "reply_bn": "প্রতিদিন ১টি আয়রন-ফলিক অ্যাসিড (IFA) ও ১টি ক্যালসিয়াম ট্যাবলেট খান। মনে রাখবেন: আয়রন ও ক্যালসিয়াম একসাথে খাবেন না—দুটির মাঝে অন্তত ২ ঘণ্টা বিরতি দিন (যেমন: দুপুরে ক্যালসিয়াম ও রাতে আয়রন)।",
        "reply_en": "Take 1 Iron-Folic Acid (IFA) tablet and 1 Calcium tablet daily. Important: Do not take Iron and Calcium together—leave at least a 2-hour gap between them for proper absorption.",
        "citation": "DGHS National Iron & Calcium Supplementation Guideline • WHO ANC (2016)"
    },
    {
        "id": "nutrition_diet",
        "keywords": ["খাবার", "পুষ্টি", "খাদ্য", "ডায়েট", "ফল", "দুধ", "ডিম", "food", "eat", "diet", "nutrition"],
        "emergency": False,
        "reply_bn": "প্রতিদিনের খাবারে ডিম, মাছ, মাংস বা ডাল (প্রোটিন), শাকসবজি (আয়রন ও ফলিক অ্যাসিড), দুধ/দই (ক্যালসিয়াম) এবং পর্যাপ্ত বিশুদ্ধ পানি রাখুন। কাঁচা বা আধাসিদ্ধ খাবার ও অতিরিক্ত ক্যাফেইন এড়িয়ে চলুন।",
        "reply_en": "Include eggs, fish, lentils (protein), leafy greens (iron & folic acid), milk/yogurt (calcium), and plenty of safe water daily. Avoid raw/undercooked meat, unpasteurized dairy, and excess caffeine.",
        "citation": "WHO Maternal Nutrition Guideline • Bangladesh ANC Handbook"
    },
    {
        "id": "vaccine_tt_epi",
        "keywords": ["টিকা", "টিটি", "ভ্যাকসিন", "ইপিআই", "vaccine", "tt", "tetanus", "epi"],
        "emergency": False,
        "reply_bn": "গর্ভাবস্থায় টিটি (TT) টিকা মা ও নবজাতককে ধনুষ্টংকার থেকে সুরক্ষা দেয়। আপনার ANC কার্ড অনুযায়ী নির্ধারিত তারিখে নিকটস্থ ইপিআই কেন্দ্র বা উপজেলা স্বাস্থ্য কমপ্লেক্স থেকে টিকা নিন।",
        "reply_en": "TT (Tetanus Toxoid) vaccination protects both mother and newborn. Follow your ANC card schedule at the nearest EPI center or Upazila Health Complex.",
        "citation": "DGHS Bangladesh EPI & Maternal Immunization Schedule"
    }
]


def query_clinical_rag(question: str, lang: str = "bn") -> Dict[str, Any]:
    q_lower = question.lower()
    best_match = None
    best_score = 0

    for doc in CLINICAL_KB:
        score = sum(1 for kw in doc["keywords"] if kw in q_lower)
        if score > best_score:
            best_score = score
            best_match = doc

    if best_match:
        return {
            "answer": best_match["reply_bn"] if lang == "bn" else best_match["reply_en"],
            "citation": best_match["citation"],
            "emergency": best_match["emergency"],
            "matched_doc": best_match["id"]
        }

    # ডিফল্ট নিরাপদ উত্তর
    default_bn = "ধন্যবাদ! গর্ভাবস্থায় নিয়মিত ANC চেকআপ, পুষ্টিকর খাবার, পর্যাপ্ত বিশ্রাম এবং প্রতিদিন আয়রন-ক্যালসিয়াম গ্রহণ করুন। কোনো বিপদচিহ্ন (রক্তক্ষরণ, তীব্র মাথাব্যথা, জ্বর বা বাচ্চার নড়াচড়া কম) দেখা দিলে দ্রুত হাসপাতালে যোগাযোগ করুন।"
    default_en = "Thank you! Maintain regular ANC checkups, balanced nutrition, adequate rest, and daily IFA/Calcium supplements. If you notice any danger signs (bleeding, severe headache, fever, or reduced fetal movement), seek medical care immediately."
    return {
        "answer": default_bn if lang == "bn" else default_en,
        "citation": "WHO ANC 8-Contact Guideline (2016) • DGHS Bangladesh",
        "emergency": False,
        "matched_doc": "general_anc"
    }