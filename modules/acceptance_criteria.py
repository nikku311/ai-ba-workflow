from utils.gemini_client import get_gemini_client

AC_SYSTEM_INSTRUCTION = """You are a Technical Business Analyst specializing in Acceptance Criteria.
Create comprehensive ACs using Given-When-Then format. Include positive, negative, and edge cases."""

def generate_acceptance_criteria(user_story: str, additional_context: str = "") -> str:
    prompt = f"""Based on this User Story, create comprehensive Acceptance Criteria:
    
    USER STORY:
    {user_story}
    
    {f"ADDITIONAL CONTEXT: {additional_context}" if additional_context else ""}
    
    Please provide:
    
    1. **Positive Scenarios** (Happy Path):
       - Given-When-Then format mein
       - Minimum 3 scenarios
    
    2. **Negative Scenarios** (Error Cases):
       - Kya-kya galat ho sakta hai
       - Invalid inputs, edge cases
    
    3. **Boundary/Edge Cases:**
       - Extreme values
       - Null/empty cases
       - Maximum limits
    
    4. **UI/UX Validation** (if applicable):
       - Field validations
       - Error messages
    
    5. **Performance Criteria**:
       - Response time expectations
       - Load handling
    
    Format har scenario ko clearly alag-alag dikhana. Numbering use karo."""

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': AC_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in acceptance criteria generator: {str(e)}"


def validate_story_completeness(user_story: str) -> str:
    prompt = f"""Review this User Story for completeness and quality:
    
    {user_story}
    
    Check against INVEST criteria:
    - Independent: Kisi aur story pe depend toh nahi?
    - Negotiable: Discussion ke liye open hai?
    - Valuable: User ko value de rahi hai?
    - Estimable: Dev team estimate kar sakti hai?
    - Small: Ek sprint mein complete ho sakti hai?
    - Testable: Test karne layak hai?
    
    Score each (1-5) and give improvement suggestions."""

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': AC_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in validation: {str(e)}"