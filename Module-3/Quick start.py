import os
from dotenv import load_dotenv
from openai import OpenAI

#Loand API key from .env file
load_dotenv()

#Initialize the OpenAI client

client =OpenAI(api_key=os.getenv("OPENAI_API_KEY"))





