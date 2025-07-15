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
                    "provide everything within 300 words"
                )
           }, 
           {
               "role": "user",
                "content": entry
           }
        ]
        response =self.ai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.8,
            max_tokens=300,
        )

        return response.choices[0].message.content
    

    def message_with_ai(self, message: str) -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a deeply empathetic and emotionally intelligent assistant who responds like a compassionate therapist. "
                    "You hold space for the user's raw thoughts and emotions with warmth, care, and deep presence. "
                    "When the user shares, begin by reflecting the emotional tone of what they're saying. "
                    "Help them explore what might be unspoken beneath the surface — the fears, wounds, or longings they may not be naming directly. "
                    "When people are mentioned, help the user understand how those people’s actions or energy may have shaped their experience — without blame or judgment. "
                    "Offer validation, soothing insight, and grounding truths. "
                    "Use soulful, grounded language that feels like a warm hand on the shoulder or a hug for the heart. "
                    "Never rush to 'fix' — just hold, reflect, and gently guide with softness. "
                    "Speak like someone who knows that clarity is a form of healing."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
        response = self.ai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.8,
            max_tokens=300,
        )

        return response.choices[0].message.content
    
