# Importing new functions from gemini_client file of utils folder
from utils.gemini_client import get_gemini_client

def generate_user_story(requirement: str, model_choice: str) -> str:
    """
    Generating User Story and Acceptance Criteria from user requirements
    """
    
    # Set name according to the model from the sidebar of the app
    selected_model = 'gemini-2.5-flash' # Default Model
    if "pro" in model_choice.lower():
        selected_model = 'gemini-2.5-pro'

    # System Instruction for AI
    system_msg = """You are a senior Business Analyst with 10 years of experience. 
Create detailed user stories in proper format."""

    # Prompt given to the AI
    prompt = f"""
Create a user story for this requirement:
{requirement}

Format:
As a [type of user], I want [goal] so that [benefit].

Also provide:
- Acceptance Criteria (Given-When-Then format)
- Priority (High/Medium/Low)
- Story Points (1-13)
"""

    try:
        # Call Gemini Client
        client = get_gemini_client()
        
        # Generate response acccording to the selected model
        response = client.models.generate_content(
            model=selected_model,
            contents=prompt,
            config={'system_instruction': system_msg}
        )
        return response.text
        
    except Exception as e:
        return f"Error in requirement generator: {str(e)}"
