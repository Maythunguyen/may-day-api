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
                    "You are an assistant that analyzes journal entries. "
                    "Your job is to identify names of people mentioned in the reflection "
                    "and determine whether they bring positive or negative influence. "
                    "give recommendations or a deep talk based on the analysis. "
                )
           }, 
           {
               "role": "user",
                "content": entry
           }
        ]
        response =self.ai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150,
        )

        return response.choices[0].message.content
    
    def analyse_bulk_entries(self, all_entries):
        messages = [
           {
               "role": "system",
               "content": (
                    "You are an assistant that analyzes journal entries. "
                    "Your job is to identify names of people mentioned in the reflection "
                    "and determine whether they bring positive or negative influence. "
                    "If someone is mentioned repeatedly in a negative light, raise a concern. "
                    "If someone is mentioned positively, respond with encouragement. "
                    "Use phrases like:\n\n"
                    "- 'Keep up with this person' if their influence is mostly positive.\n"
                    "- 'This person may be bringing more negativity than positivity. Consider setting boundaries.'\n"
                    "- Only analyze based on the provided text. Respond briefly and clearly."
                )
           }, 
           {
               "role": "user",
                "content": all_entries
           }
        ]
        bulk_response =self.ai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150,
        )

        return bulk_response.choices[0].message.content

       