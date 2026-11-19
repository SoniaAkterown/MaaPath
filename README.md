<p align="center">
  <img src="https://img.magnific.com/premium-vector/pregnant-woman-with-blue-white-logo-that-says-mother_1119689-196.jpg" alt="MaaPath AI Logo" width="160" style="border-radius: 20px;">
</p>

<h1 align="center">MaaPath AI 🩺</h1>

<h3 align="center">AI-Powered Maternal & Newborn Safety Navigator for Bangladesh (LangGraph Multi-Agent System)</h3>

<p align="center">
  <img src="https://img.shields.io/github/stars/SoniaAkterown/MaaPath?style=flat&logo=github&color=yellow" alt="Stars">
  <img src="https://komarev.com/ghpvc/?username=SoniaAkterown&repo=MaaPath&label=views&color=blue&style=flat" alt="Views">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115.0-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/LangGraph-0.2.35-1C3C3C?style=flat" alt="LangGraph">
  <img src="https://img.shields.io/badge/LangChain-0.3.10-121212?style=flat" alt="LangChain">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.35-D71F00?style=flat" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=flat&logo=supabase&logoColor=white" alt="Supabase">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Uvicorn-0.30.6-499848?style=flat" alt="Uvicorn">
  <img src="https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=flat&logo=render&logoColor=black" alt="Render">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
</p>

<p align="center">
  <a href="https://maapath.onrender.com"><strong>🌐 Live Web App</strong></a> •
  <a href="https://maapath.onrender.com/docs"><strong>📡 FastAPI Swagger Docs</strong></a> •
  <a href="#-demo-walkthrough-for-collaborators--judges"><strong>🎮 Demo Walkthrough</strong></a>
</p>

---

## Contributors 👥

<p align="center">
  <a href="https://github.com/SoniaAkterown">
    <img src="https://github.com/SoniaAkterown.png" width="65px;" style="border-radius: 50%;" alt="Sonia Akter"/>
  </a>
  <a href="https://github.com/ashfiqadnan">
    <img src="https://github.com/ashfiqadnan.png" width="65px;" style="border-radius: 50%;" alt="Ashfiq Adnan"/>
  </a>
  <a href="https://github.com/mdshadin751">
    <img src="https://github.com/mdshadin751.png" width="65px;" style="border-radius: 50%;" alt="Md Shadin"/>
  </a>
</p>

---

# 🩺 MaaPath AI

**MaaPath AI** is not a standard pregnancy tracking app—it is an **AI-Powered Maternal & Newborn Care Coordination System** engineered for Bangladesh. It unites expectant mothers, community health workers (CHWs), and public healthcare facilities (**Upazila Health Complexes & District Hospitals**) through a **LangGraph Multi-Agent Architecture**, bilingual (**English & বাংলা**) Clinical RAG guidance, deterministic danger-sign triage, and automated ANC planning.

> **Live Application:** [https://maapath.onrender.com](https://maapath.onrender.com)  
> **API Documentation:** [https://maapath.onrender.com/docs](https://maapath.onrender.com/docs)

> ⚠️ **Crucial Medical Disclaimer:** MaaPath AI does **not** diagnose diseases. It provides clinical alerts, educational guidance, and emergency hospital referral pathways strictly aligned with **WHO Antenatal Care (ANC) Guidelines** and **DGHS Bangladesh** maternal health protocols.

---

## 🎯 Core 3-Pillar Strategy

1. **🔮 Predictive Intelligence:** Analyzes maternal vitals (BP, Hemoglobin, Blood Sugar, Weight) and obstetric history to flag potential clinical risks early (e.g., Pre-eclampsia, Gestational Diabetes, Anemia).
2. **🤖 Agentic Decision Support:** Orchestrates specialized AI agents via **LangGraph** to coordinate ANC checkups, lab tests, and hospital referral pathways.
3. **❤️ Continuity of Care:** Provides end-to-end maternal and newborn tracking from early pregnancy registration through delivery preparation and postnatal **Bangladesh EPI** vaccination follow-ups.

---

## 🏗️ LangGraph Multi-Agent Architecture

MaaPath AI uses a deterministic-first **LangGraph State Machine** so life-threatening danger signs bypass LLM latency and trigger immediate hospital escalation.

```text
Mother Registration / Vitals / Bangla-EN Query
                      │
                      ▼
            [ 1. Intake Agent ]
     (Calculates EDD, Gestational Week & Trimester)
                      │
                      ▼
        [ 2. Risk Screening Agent ]
  (Deterministic Clinical Guardrail: 7 Danger Signs)
                      │
         ┌────────────┴────────────┐
         │ Emergency Detected?     │ Routine / Safe
         ▼                         ▼
 [ 3. Referral Agent ]     ┌───────┴───────────────┐
 (Immediate Escalation     ▼                       ▼
  to UHC / District  [ 4. ANC Planning ]   [ 5. Clinical RAG ]
   Hospital & 999)    (WHO Visit Schedule)  (WHO & DGHS Verified)
```

### Specialized Agent Roles
- **Intake Agent:** Collects demographics, Last Menstrual Period (LMP), blood group, and obstetric history; auto-calculates Expected Delivery Date (EDD).
- **Risk Screening Agent:** Executes deterministic rule-based screening for 7 critical maternal danger signs (bleeding, severe headache, blurred vision, convulsions, high fever, severe abdominal pain, reduced fetal movement).
- **ANC Planning Agent:** Organizes WHO-recommended Antenatal Care (ANC) schedules, ultrasound milestones, and IFA/Calcium supplementation reminders.
- **Clinical RAG Agent:** Answers bilingual (**বাংলা & English**) maternal health queries backed by verified WHO & DGHS citations.
- **Referral Agent:** Matches risk urgency with nearby **Upazila Health Complexes (UHC)** and **District Hospitals**, dispatching structured digital referral slips.
- **Follow-up & Newborn Care Agents:** Tracks missed appointments, postnatal maternal recovery, and **Bangladesh EPI** immunization schedules.

---

## ✨ 14 Integrated UI Modules (Bilingual EN / বাংলা + Dark/Light Mode)

| Category | Modules Included |
| :--- | :--- |
| **A. Mother & Pregnancy Care** | `1. Mother Dashboard` • `2. Mother Registration` • `3. Pregnancy Management` • `4. Health Monitoring` • `5. Risk Assessment` • `6. ANC Planning` |
| **B. AI, Referral & Newborn** | `7. Bangla Clinical RAG AI Assistant` • `8. Smart Hospital Referral` • `9. Newborn Care & EPI Tracker` |
| **C. Care Team, Admin & Ops** | `10. Health Worker Dashboard` • `11. Admin Dashboard` • `12. AI Agent Monitoring (Human-in-the-Loop)` |
| **D. Alerts & Preferences** | `13. Notification Center` • `14. Settings & Language` + **Global Emergency SOS Modal (999 & 16263)** |

---

## 🛠️ Technology Stack & Versions

- **Backend:** Python `3.11+`, FastAPI `0.115.0`, Uvicorn `0.30.6`, Pydantic `2.9.2`
- **Multi-Agent AI:** LangGraph `0.2.35`, LangChain Core `0.3.10`, Verified Clinical RAG
- **Database:** PostgreSQL (**Supabase Session Pooler**), SQLAlchemy `2.0.35`, `psycopg2-binary` (with automatic local SQLite fallback)
- **Frontend:** Responsive SPA built with HTML5, Tailwind CSS, Vanilla JavaScript, FontAwesome 6, and Google Fonts (*Inter* & *Hind Siliguri*)
- **Cloud Deployment:** Render Web Service ([maapath.onrender.com](https://maapath.onrender.com))

---

## 📁 Directory Structure

```text
MaaPath/
├── backend/
│   ├── main.py             # FastAPI server, REST APIs & frontend serving
│   ├── agents.py           # LangGraph multi-agent workflow & conditional routing
│   ├── clinical_rag.py     # Verified WHO & DGHS bilingual clinical knowledge base
│   ├── database.py         # SQLAlchemy models (Mother, VitalLog, ANCVisit, Referral)
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # Complete 14-module bilingual responsive UI + Pregnancy Guide
└── README.md
```

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/SoniaAkterown/MaaPath.git](https://github.com/SoniaAkterown/MaaPath.git)
   cd MaaPath/backend
   ```

2. **Create a virtual environment & install dependencies**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Configure Environment Variables (Optional for Local)**
   Create a `.env` file inside `backend/`:
   ```env
   DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@[aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres](https://aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres)
   ```
   *(If omitted, MaaPath AI automatically uses local SQLite `maapath.db`.)*

4. **Start the FastAPI + LangGraph server**
   ```bash
   uvicorn main:app --reload
   ```
   - **Web App:** `http://127.0.0.1:8000`
   - **Interactive API Docs:** `http://127.0.0.1:8000/docs`

---

## 🎮 Demo Walkthrough (For Collaborators & Judges)

Test the end-to-end clinical workflow directly on [maapath.onrender.com](https://maapath.onrender.com):

1. **Bilingual & Theme Switch:** Toggle between **EN / বাংলা** and **Dark / Light Mode** from the top navbar to experience instant localization across all 14 modules.
2. **Smart Mother Registration (`Intake Agent`):** Click **"Register a Mother"**, enter an LMP date, and watch the live **EDD & Pregnancy Week** calculate automatically. Submit to persist the record in **Supabase PostgreSQL**.
3. **Deterministic Danger-Sign Triage (`Risk Screening Agent`):** Open **Module 5 (Risk Assessment)** and check any danger sign (e.g., *Severe Headache* or *Blurred Vision*) to trigger the immediate **HIGH EMERGENCY RISK** escalation banner.
4. **Bangla Clinical RAG (`AI Assistant`):** Open **Module 7 (AI Assistant)** and ask *"মাথা ব্যথা ও ঝাপসা দেখলে কী করব?"* (emergency bypass) or *"আয়রন ও ক্যালসিয়াম কীভাবে খাব?"* (WHO/DGHS cited response).
5. **Smart Hospital Referral (`Referral Agent`):** Open **Module 8**, filter between **Upazila Health Complexes** and **District Hospitals**, and dispatch a Digital Referral Slip.

---

## 📜 Security Policy

This project is open-source and structured for healthcare safety and transparency.
- 🛡️ **Emergency Helplines (Bangladesh):** Integrated quick-dial support for **999** (National Emergency Service) and **16263** (Shastho Batayon 24/7 Health Line).
