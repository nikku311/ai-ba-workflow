from utils.gemini_client import get_gemini_client
from config import AC_SYSTEM_INSTRUCTION, AC_PROMPT

def generate_acceptance_criteria(user_story: str) -> str:
    prompt = AC_PROMPT.format(user_story=user_story)
    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': AC_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in Acceptance Criteria generator: {str(e)}"
