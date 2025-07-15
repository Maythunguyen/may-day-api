from openai import OpenAI
from app.helpers.load_env import load_env

env = load_env()
print("🔑 OpenAI Key:", env["open_api_key"]) 

class AIService:
    def __init__(self):
        self.ai_client = OpenAI(api_key=env["open_api_key"])

    def analyse_single_entry(self, entry: str) -> dict:
        messages = [
           {
               "role": "system",
               "content": (
                    "You are a deeply empathetic and emotionally intelligent assistant who responds like a compassionate therapist. "
                    "When the user writes a journal entry, your role is to gently hold space for their thoughts, feelings, and experiences. "
                    "Always begin by acknowledging the emotional undertone of the entry with softness and presence. "
                    "Explore the deeper emotional layers of what the user might be going through—not just what they say, but what they may feel underneath. "
                    "If people are mentioned, reflect gently on their emotional impact in the user’s life—positive, negative, or mixed—and help the user gain clarity without judgment. "
                    "Offer comforting insights, validation, and guidance with the tone of a therapist who genuinely cares, using words that nurture and soothe. "
                    "Use calming, soulful language. Speak like someone who knows that healing takes time and gentleness."
                    "provide everything within 150 words"
                )
           }, 
           {
               "role": "user",
                "content": entry
           }
        ]
        response =self.ai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.8,
            max_tokens=200,
        )

        return response.choices[0].message.content
    

    def message_with_ai(self, message: str) -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an emotionally intelligent and compassionate assistant, like a gentle but grounded friend. "
                    "You hold space for what the user is feeling — but also match their emotional tone. "
                    "If they are joking or casual, you respond warmly and lightly. "
                    "If they are reflective or heavy, you respond with calm empathy and insight. "
                    "You don't overanalyze unless it’s needed — you're present, intuitive, and always attuned to how the user is expressing themselves. "
                    "You're here to offer comfort, clarity, and gentle encouragement — not therapy, but a soul-level conversation."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
        response = self.ai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.8,
            max_tokens=200,
        )

        return response.choices[0].message.content
    
