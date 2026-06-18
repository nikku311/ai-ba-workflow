# config.py - Sab prompts aur settings yahan!

# ============================================
# SYSTEM INSTRUCTIONS (BA ke liye)
# ============================================

BA_SYSTEM_INSTRUCTION = """You are a senior Business Analyst with 10 years of experience in Agile/Scrum.
You create detailed, well-structured user stories following industry best practices.
Always provide clear acceptance criteria, priorities, and story points."""

# ============================================
# PROMPTS FOR DIFFERENT MODULES
# ============================================

USER_STORY_PROMPT = """Create a comprehensive user story for the following requirement:

REQUIREMENT: {requirement}

Please provide:
1. **User Story** (As a [user], I want [goal], so that [benefit])
2. **Acceptance Criteria** (Given-When-Then format)
3. **Priority** (High/Medium/Low with justification)
4. **Story Points** (1, 2, 3, 5, 8, 13 - Fibonacci)
5. **Definition of Done**
6. **Dependencies** (if any)
7. **Risks** (if any)

Format clearly with headers and bullet points."""

ACCEPTANCE_CRITERIA_PROMPT = """Based on this User Story, create comprehensive Acceptance Criteria:

USER STORY: {user_story}

{additional_context}

Please provide:
1. **Positive Scenarios** (Happy Path) - Given-When-Then format
2. **Negative Scenarios** (Error Cases)
3. **Boundary/Edge Cases**
4. **UI/UX Validation** (if applicable)
5. **Performance Criteria**

Format each scenario clearly with numbering."""

EMAIL_PROMPT = """Draft a professional {email_type} email with the following details:

RECIPIENT: {recipient}
SUBJECT CONTEXT: {subject_context}
TONE: {tone}

KEY POINTS:
{key_points}

Requirements:
- Clear subject line
- Professional greeting
- Structured body
- Clear call-to-action
- Professional closing

Also suggest best time to send and any follow-up needed."""

# ============================================
# MODEL SETTINGS
# ============================================

MODEL_CONFIG = {
    "default_model": "gemini-1.5-flash",
    "pro_model": "gemini-1.5-pro",
    "temperature": 0.3,
    "max_tokens": 2000
}

# ============================================
# EMAIL TEMPLATES
# ============================================

EMAIL_TEMPLATES = {
    "stakeholder_update": "Project status update",
    "requirement_clarification": "Requirement clarification needed",
    "meeting_schedule": "Meeting scheduling",
    "sign_off_request": "Sign-off request",
    "sprint_review_invite": "Sprint review invitation"
}