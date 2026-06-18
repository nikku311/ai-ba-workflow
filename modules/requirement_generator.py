from utils.gemini_client import get_gemini_client
from config import BA_SYSTEM_INSTRUCTION, USER_STORY_PROMPT

def generate_user_story(requirement: str, model_choice: str) -> str:
    selected_model = 'gemini-2.5-flash'
    if "pro" in model_choice.lower():
        selected_model = 'gemini-2.5-pro'

    prompt = USER_STORY_PROMPT.format(requirement=requirement)

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
