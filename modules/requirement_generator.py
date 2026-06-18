from utils.gemini_client import get_gemini_client

BA_SYSTEM_INSTRUCTION = """You are a senior Business Analyst with 10 years of experience in Agile/Scrum.
Create detailed, well-structured user stories following industry best practices."""

def generate_user_story(requirement: str, model_choice: str) -> str:
    selected_model = 'gemini-2.5-flash'
    if "pro" in model_choice.lower():
        selected_model = 'gemini-2.5-pro'

    prompt = f"""Create a comprehensive user story for the following requirement:

REQUIREMENT: {requirement}

Please provide:
1. **User Story** (As a [user], I want [goal], so that [benefit])
2. **Acceptance Criteria** (Given-When-Then format)
3. **Priority** (High/Medium/Low with justification)
4. **Story Points** (1, 2, 3, 5, 8, 13)
5. **Definition of Done**
6. **Dependencies** (if any)
7. **Risks** (if any)

Format clearly with headers and bullet points."""

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model=selected_model,
            contents=prompt,
            config={'system_instruction': BA_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in requirement generator: {str(e)}"