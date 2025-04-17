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
    
    def analyse_bulk_entries(self, all_entries):
        messages = [
        {
            "role": "system",
            "content": (
                "You are a deeply empathetic and emotionally intelligent assistant who responds like a compassionate therapist. "
                "When the user writes journal entries, your role is to provide a summary of emotional patterns based on the people mentioned. "
                "Gently analyze how these individuals influence the user's emotional state — whether positively, negatively, or mixed. "
                "For each person mentioned across multiple entries, reflect on their emotional impact and provide a short insight. "
                "Use emotionally sensitive and non-judgmental language. Your tone should be validating, calm, and soothing. "
                "Your response must be strictly in the following JSON format:"
                "\n\n"
                "[\n"
                "  {\n"
                "    \"name\": \"[Person's name]\",\n"
                "    \"insight\": \"[Short therapeutic insight about how this person makes the user feel, e.g. their emotional impact, pattern, and any gentle guidance.]\"\n"
                "  },\n"
                "  ...\n"
                "]"
                "\n\n"
                "Only include people who appear more than once or are emotionally significant. Do not include irrelevant content or extra commentary outside the JSON."
            )
        },
        {
            "role": "user",
            "content": all_entries
        }
        ]
        bulk_response =self.ai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.8,
            max_tokens=300,
        )

        return bulk_response.choices[0].message.content

       