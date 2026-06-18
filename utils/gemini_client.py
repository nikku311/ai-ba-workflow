import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

# Initialize Gemini Client
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: GEMINI_API_KEY .env फ़ाइल में नहीं मिली!")
    return genai.Client(api_key=api_key)

# Main function to get answer from AI
def get_gemini_response(prompt: str, system_msg: str = "You are a helpful assistant") -> str:
    try:
        client = get_gemini_client()
        # Using lates and fast gemini model 'gemini-2.5-flash'
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'system_instruction': system_msg}
        )
        return response.text
    except Exception as e:
        return f"Error connecting to Gemini: {str(e)}"
