# config.py - Sab prompts aur settings yahan!

# System messages for different modules
SYSTEM_PROMPTS = {
    "user_story": """You are a senior Business Analyst with 10 years of experience in Agile/Scrum.
Create detailed, well-structured user stories following industry best practices.""",
    
    "acceptance_criteria": """You are a Technical Business Analyst specializing in Acceptance Criteria.
Create comprehensive ACs using Given-When-Then format. Include positive, negative, and edge cases.""",
    
    "email_drafter": """You are a professional Business Analyst who communicates effectively with stakeholders.
Draft clear, concise, and professional emails suitable for corporate environments."""
}

# Model settings
MODEL_CONFIG = {
    "default_model": "gemini-1.5-flash",
    "temperature": 0.3,  # Kam temperature = zyada focused, predictable output
    "max_tokens": 2000
}

# Email templates ke liye placeholders
EMAIL_TEMPLATES = {
    "stakeholder_update": "Project status update bhejna",
    "requirement_clarification": "Requirement clear karne ke liye",
    "meeting_schedule": "Meeting fix karne ke liye",
    "sign_off_request": "Sign-off maangne ke liye"
}