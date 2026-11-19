import os
from groq import Groq

# Verified WHO & DGHS Bangladesh Clinical Knowledge Base (Grounding Context)
CLINICAL_KB = """
1. Iron & Calcium Supplementation (DGHS Bangladesh):
   - Take 1 Iron-Folic Acid (IFA) tablet and 1 Calcium tablet daily during pregnancy.
   - Never take Iron and Calcium together; keep at least a 2-hour gap (e.g., Calcium after lunch, Iron after dinner).
2. WHO Antenatal Care (ANC) Schedule:
   - Minimum 4 to 8 ANC visits: 1st visit before 12 weeks, then at 20, 26, 30, 34, 36, 38, and 40 weeks.
   - Monitor Blood Pressure, Weight, Urine Protein, and Hemoglobin regularly.
3. 7 Maternal Danger Signs (Immediate Emergency Referral):
   - Vaginal bleeding, severe headache, blurred vision, convulsions/fits, high fever, severe abdominal pain, or reduced fetal movement.
   - Action: Go immediately to the nearest Upazila Health Complex (UHC) or District Hospital. Call 999 (Emergency) or 16263 (Shastho Batayon).
4. Newborn Care & Bangladesh EPI:
   - Initiate breastfeeding within 1 hour of birth; exclusive breastfeeding for 6 months.
   - BCG & OPV-0 at birth; Pentavalent, PCV, OPV at 6, 10, 14 weeks; MR at 9 months.
"""

def query_clinical_rag(user_query: str, language: str = "bn") -> dict:
    api_key = os.getenv("GROQ_API_KEY")

    # Groq LLM দিয়ে আসল Clinical RAG উত্তর
    if api_key:
        try:
            client = Groq(api_key=api_key)
            system_prompt = f"""
You are MaaPath AI, a compassionate Maternal & Newborn Safety Navigator for Bangladesh.
Use ONLY the verified clinical context below and standard WHO/DGHS Bangladesh guidelines.
Rules:
1. NEVER diagnose diseases. Give clear, safe guidance and advise visiting a doctor/UHC when needed.
2. Reply in the SAME language the user used (Bangla or English). Keep answers concise (3-4 sentences).
3. If any danger sign is mentioned, instruct immediate hospital visit and mention 999 / 16263.

Verified Context:
{CLINICAL_KB}
"""
            chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query}
                ],
                temperature=0.3,
                max_tokens=300
            )
            answer = chat_completion.choices[0].message.content.strip()
            return {
                "answer": answer,
                "source": "WHO ANC & DGHS Bangladesh Guidelines • Verified via Groq Clinical RAG"
            }
        except Exception as e:
            print(f"Groq API error: {e}")

    # Fallback (যদি কোনো কারণে API Key না থাকে)
    q = user_query.lower()
    if any(k in q for k in ["iron", "calcium", "আয়রন", "ক্যালসিয়াম", "ট্যাবলেট"]):
        return {
            "answer": "গর্ভাবস্থায় প্রতিদিন ১টি আয়রন-ফলিক অ্যাসিড (IFA) ও ১টি ক্যালসিয়াম ট্যাবলেট খাওয়া জরুরি। তবে দুটো একসাথে খাবেন না—কমপক্ষে ২ ঘণ্টা বিরতি দিন (যেমন: দুপুরে ক্যালসিয়াম ও রাতে আয়রন)।",
            "source": "DGHS National Iron & Calcium Guideline • Verified"
        }
    return {
        "answer": "আপনার প্রশ্নের জন্য ধন্যবাদ। নিয়মিত ANC চেকআপ করান, পুষ্টিকর খাবার খান এবং যেকোনো জরুরি লক্ষণে নিকটস্থ উপজেলা স্বাস্থ্য কমপ্লেক্সে যোগাযোগ করুন বা ১৬২৬৩ নম্বরে কল করুন।",
        "source": "WHO & DGHS Bangladesh Maternal Care Protocol • Verified"
    }
