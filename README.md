# 🤖 AI BA Workflow — Intelligent Business Analyst Copilot

**Check the app -** https://ai-ba-workflow-dqx8xhnu7dcwqwbadh2rcr.streamlit.app/

&gt; **An AI-powered workflow automation tool that transforms raw business requirements into production-ready user stories, acceptance criteria, and stakeholder communications — built for enterprise Business Analysts.**

---

## 🎯 Problem Statement

**Traditional BA workflow is manual, inconsistent, and time-consuming:**

| Step | Manual Effort | Time | Error Rate |
|------|-------------|------|------------|
| Requirement gathering | High | 2-3 hours | 15-20% |
| User story creation | High | 1-2 hours | 10-15% |
| Acceptance criteria drafting | High | 1-2 hours | 20-25% |
| Stakeholder communication | Medium | 30-45 min | 10-12% |
| **Total per requirement** | **Very High** | **5-8 hours** | **15-20%** |

**This tool reduces it to 5-10 minutes with AI-generated, standardized outputs.**

---

## 🏗️ Architecture

```mermaid
graph TD
    A[User Input: Business Requirement] --&gt; B{Module Router}
    B --&gt;|User Stories| C[Requirement Generator]
    B --&gt;|Acceptance Criteria| D[AC Generator]
    B --&gt;|Emails| E[Email Drafter]
    
    C --&gt; F[Google Gemini API]
    D --&gt; F
    E --&gt; F
    
    F --&gt; G[Structured Output]
    G --&gt; H[Streamlit UI]
    H --&gt; I[User Review & Download]
    
    style A fill:#e1f5fe
    style F fill:#fff3e0
    style I fill:#e8f5e9

**🛠️ Tech Stack**

| Layer               | Technology                  | Purpose                        |
| ------------------- | --------------------------- | ------------------------------ |
| **LLM Engine**      | Google Gemini 2.5 Flash/Pro | Text generation & reasoning    |
| **Language**        | Python 3.10+                | Core application logic         |
| **UI Framework**    | Streamlit                   | Rapid prototyping & deployment |
| **API Client**      | `google-generativeai`       | LLM SDK integration            |
| **Environment**     | `python-dotenv`             | Secure API key management      |
| **Version Control** | Git + GitHub                | Source control                 |
| **Deployment**      | Streamlit Cloud             | Serverless PaaS                |

**📁 Project Structure**

ai-ba-workflow/
├── app.py                          # Main Streamlit application
├── config.py                       # Centralized prompts & settings
├── requirements.txt                # Dependency management
├── .env                            # API keys (gitignored)
├── modules/                        # Core BA logic
│   ├── __init__.py
│   ├── requirement_generator.py   # User story generation
│   ├── acceptance_criteria.py     # AC generation with GWT format
│   └── email_drafter.py          # Stakeholder communication
├── utils/                          # Reusable utilities
│   ├── __init__.py
│   └── gemini_client.py          # LLM API wrapper
└── data/
    └── sample_requirements.json  # Demo dataset

**✨ Features**

**Module 1: User Story Generator**

Input: Raw business requirement

Output: Structured user story with:
As a [user], I want [goal], so that [benefit]
Acceptance Criteria (Given-When-Then)
Priority (High/Medium/Low)
Story Points (Fibonacci: 1, 2, 3, 5, 8, 13)
Definition of Done
Dependencies & Risks

**Module 2: Acceptance Criteria Generator**

Input: User story + optional context
Output: Comprehensive ACs with:
Positive scenarios (Happy path)
Negative scenarios (Error cases)
Boundary/Edge cases
UI/UX validation rules
Performance criteria

**Module 3: Email Drafting**

Stakeholder Emails: Professional communication templates
Meeting Minutes: Automated minutes generation
Tone Customization: Formal / Professional / Friendly / Urgent
