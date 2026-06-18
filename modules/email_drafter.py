from utils.gemini_client import get_gemini_response
from config import SYSTEM_PROMPTS, EMAIL_TEMPLATES

def draft_stakeholder_email(
    email_type: str,
    recipient: str,
    subject_context: str,
    key_points: list,
    tone: str = "professional"
) -> str:
    """
    Professional stakeholder emails draft karta hai
    
    Parameters:
        email_type: Kaisa email (update, clarification, meeting, sign-off)
        recipient: Kis ko bhejna hai (Product Owner, Dev Team, Client)
        subject_context: Email kis baare mein hai
        key_points: Main points jo cover karne hain
        tone: professional/friendly/urgent
    
    Returns:
        Complete email draft
    """
    
    points_formatted = "\n".join([f"- {point}" for point in key_points])
    
    prompt = f"""
    Draft a professional email with the following details:
    
    EMAIL TYPE: {email_type}
    RECIPIENT: {recipient}
    SUBJECT: {subject_context}
    TONE: {tone}
    
    KEY POINTS TO COVER:
    {points_formatted}
    
    Requirements:
    - Clear subject line
    - Professional greeting
    - Structured body (paragraphs/bullet points)
    - Clear call-to-action (kya chahiye recipient se)
    - Professional closing
    - Signature placeholder
    
    Also suggest:
    - Best time to send this email
    - Any attachments needed
    - Follow-up timeline
    """
    
    return get_gemini_response(prompt, SYSTEM_PROMPTS["email_drafter"])


def draft_meeting_minutes(
    meeting_title: str,
    attendees: list,
    agenda: str,
    decisions: list,
    action_items: list
) -> str:
    """
    Meeting ke baad minutes draft karta hai
    """
    
    attendees_str = ", ".join(attendees)
    decisions_str = "\n".join([f"{i+1}. {d}" for i, d in enumerate(decisions)])
    action_items_str = "\n".join([
        f"{i+1}. {item['task']} - Owner: {item['owner']} - Due: {item['due_date']}"
        for i, item in enumerate(action_items)
    ])
    
    prompt = f"""
    Create professional Meeting Minutes for:
    
    MEETING: {meeting_title}
    ATTENDEES: {attendees_str}
    AGENDA: {agenda}
    
    DECISIONS MADE:
    {decisions_str}
    
    ACTION ITEMS:
    {action_items_str}
    
    Format as formal meeting minutes with:
    - Header (date, time, location)
    - Attendees list
    - Agenda summary
    - Detailed discussion points
    - Decisions (clearly highlighted)
    - Action items table (Task | Owner | Due Date | Status)
    - Next meeting date placeholder
    """
    
    return get_gemini_response(prompt, SYSTEM_PROMPTS["email_drafter"])


def get_email_template_options():
    """
    UI ke liye available email types return karta hai
    """
    return list(EMAIL_TEMPLATES.keys())