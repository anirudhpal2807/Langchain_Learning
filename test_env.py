import time
import sys
print("Starting test script...")
print(f"Python: {sys.executable}")
time.sleep(1)
print("Environment seems okay!")
try:
    from dotenv import load_dotenv
    load_dotenv("../.env")
    print("Dotenv loaded!")
except Exception as e:
    print(f"Dotenv error: {e}")

try:
    import langchain
    print(f"Langchain version: {langchain.__version__}")
except Exception as e:
    print(f"Langchain error: {e}")
