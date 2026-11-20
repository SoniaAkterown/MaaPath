# Security & Clinical Safety Policy 

## Supported Versions

The following versions of **MaaPath AI** are currently supported with security and clinical safety updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

---

## Reporting a Vulnerability

We take security and patient data privacy seriously. If you discover a security vulnerability in **MaaPath AI**, please report it responsibly:

1. **Do not** open a public GitHub issue for sensitive security vulnerabilities.
2. Use GitHub's **Private Vulnerability Reporting** (under the **Security** tab → **Advisories** → **Report a vulnerability**) or contact the repository maintainers directly via GitHub.
3. Include a clear description of the issue, steps to reproduce, and potential impact.

We will acknowledge your report within **48 hours** and work to resolve verified issues promptly.

---

## Data Privacy & Secret Management

- **Environment Variables:** Sensitive credentials (`GROQ_API_KEY`, `DATABASE_URL`) are strictly managed via `.env` files locally and encrypted Environment Variables on Render—never committed to source control.
- **Patient Data:** Maternal health records stored in Supabase PostgreSQL are intended strictly for care coordination, ANC tracking, and emergency referrals with informed consent.

---

## Clinical Safety Guardrails 🩺

- **Not a Medical Diagnosis Tool:** MaaPath AI provides WHO & DGHS Bangladesh-aligned educational guidance and triage support; it **never** diagnoses diseases or replaces a licensed physician.
- **Deterministic Emergency Override:** The 7 critical maternal danger signs bypass LLM generation to immediately trigger hospital referral pathways and Bangladesh emergency helplines (**999** — National Emergency Service, **16263** — Shastho Batayon).
