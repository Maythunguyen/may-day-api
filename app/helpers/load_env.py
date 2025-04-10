from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "open_api_key": os.getenv("OPENAI_API_KEY"),
    }