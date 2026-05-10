import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    response = llm.invoke("Hello, how are you?")
    print("Success!")
    print(response.content)
except Exception as e:
    print(f"Error: {e}")
