from utils.gemini_client import get_gemini_client
from config import EMAIL_SYSTEM_INSTRUCTION, EMAIL_PROMPT

def draft_stakeholder_email(user_story: str, criteria: str) -> str:
    prompt = EMAIL_PROMPT.format(user_story=user_story, criteria=criteria)
    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': EMAIL_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in Email Drafter: {str(e)}"
