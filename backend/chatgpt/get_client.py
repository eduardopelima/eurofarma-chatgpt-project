from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

class OpenAIClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv(find_dotenv())
            cls._instance = super(OpenAIClient, cls).__new__(cls)
            api_key = os.environ.get("OPENAI_API_KEY")
            cls._instance.client = OpenAI(api_key=api_key)
        return cls._instance
