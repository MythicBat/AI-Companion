import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def ask_companion(message):
    """
    Sends the user's message to OpenAI and returns a kind response
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a supportive spring-themed mental health companion named Jarvis. "
                        "Your goal is to offer empathy, encouragment, and practical mental wellness tips "
                        "for users feeling down or anxious during seasonal changes. Keep it short and warm."
                    ),
                },
                {
                    "role": "user",
                    "content": message,
                }
            ],
            temperature=0.8,
            max_tokens=100
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return "Sorry! I couldn't reach the AI brain right now. Try again later "