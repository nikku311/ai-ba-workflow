# config.py - Prompts and settings

BA_SYSTEM_INSTRUCTION = """You are a senior Business Analyst with 10 years of experience. 
Create highly professional and detailed business analyst documents based on the inputs provided."""

USER_STORY_PROMPT = """
Create a comprehensive user story for this requirement:
{requirement}

Format:
As a [type of user], I want [goal] so that [benefit].

Also provide:
- Priority (High/Medium/Low)
- Story Points (1-13)
"""

AC_SYSTEM_INSTRUCTION = "You are an expert QA and Business Analyst. Create exhaustive acceptance criteria."
AC_PROMPT = """
Based on this User Story, create detailed Acceptance Criteria using the Given-When-Then format for all possible scenarios (Positive, Negative, and Edge cases):

{user_story}

Provide clear bullet points.
"""

EMAIL_SYSTEM_INSTRUCTION = "You are a professional Business Analyst. Write clear, corporate-ready emails."
EMAIL_PROMPT = """
Draft a professional email to send to the development team and stakeholders introducing the newly created User Story and Acceptance Criteria.

User Story:
{user_story}

Acceptance Criteria:
{criteria}

The email should include:
- A clear Subject Line
- A professional greeting
- A brief summary of what this requirement achieves
- The User Story and AC neatly presented
- A call-to-action for feedback or review
- A professional sign-off (leave placeholders like [Your Name])
"""
