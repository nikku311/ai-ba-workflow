from utils.gemini_client import get_gemini_response
from config import SYSTEM_PROMPTS

def generate_acceptance_criteria(user_story: str, additional_context: str = "") -> str:
    """
    User Story se detailed Acceptance Criteria generate karta hai
    
    Parameters:
        user_story: Pehle se bani user story
        additional_context: Extra info (optional)
    
    Returns:
        Formatted ACs with Given-When-Then + edge cases
    """
    
    prompt = f"""
    Based on this User Story, create comprehensive Acceptance Criteria:
    
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
    
    Format har scenario ko clearly alag-alag dikhana. Numbering use karo.
    """
    
    return get_gemini_response(prompt, SYSTEM_PROMPTS["acceptance_criteria"])


def validate_story_completeness(user_story: str) -> str:
    """
    Check karta hai ki user story INVEST principle follow karti hai ya nahi
    
    INVEST = Independent, Negotiable, Valuable, Estimable, Small, Testable
    """
    
    prompt = f"""
    Review this User Story for completeness and quality:
    
    {user_story}
    
    Check against INVEST criteria:
    - Independent: Kisi aur story pe depend toh nahi?
    - Negotiable: Discussion ke liye open hai?
    - Valuable: User ko value de rahi hai?
    - Estimable: Dev team estimate kar sakti hai?
    - Small: Ek sprint mein complete ho sakti hai?
    - Testable: Test karne layak hai?
    
    Score each (1-5) and give improvement suggestions.
    """
    
    return get_gemini_response(prompt, SYSTEM_PROMPTS["acceptance_criteria"])