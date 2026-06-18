from utils.gemini_client import get_gemini_client

EMAIL_SYSTEM_INSTRUCTION = """You are a professional Business Analyst who communicates effectively with stakeholders.
Draft clear, concise, and professional emails suitable for corporate environments."""

EMAIL_TEMPLATES = {
    "stakeholder_update": "Project status update bhejna",
    "requirement_clarification": "Requirement clear karne ke liye",
    "meeting_schedule": "Meeting fix karne ke liye",
    "sign_off_request": "Sign-off maangne ke liye"
}

def draft_stakeholder_email(email_type: str, recipient: str, subject_context: str, key_points: list, tone: str = "professional") -> str:
    points_formatted = "\n".join([f"- {point}" for point in key_points])
    
    prompt = f"""Draft a professional email with the following details:
    
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
    - Follow-up timeline"""

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': EMAIL_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in email drafter: {str(e)}"


def draft_meeting_minutes(meeting_title: str, attendees: list, agenda: str, decisions: list, action_items: list) -> str:
    attendees_str = ", ".join(attendees)
    decisions_str = "\n".join([f"{i+1}. {d}" for i, d in enumerate(decisions)])
    action_items_str = "\n".join([
        f"{i+1}. {item['task']} - Owner: {item['owner']} - Due: {item['due_date']}"
        for i, item in enumerate(action_items)
    ])
    
    prompt = f"""Create professional Meeting Minutes for:
    
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
    - Next meeting date placeholder"""

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': EMAIL_SYSTEM_INSTRUCTION}
        )
        return response.text
    except Exception as e:
        return f"Error in meeting minutes: {str(e)}"


def get_email_template_options():
    return list(EMAIL_TEMPLATES.keys())