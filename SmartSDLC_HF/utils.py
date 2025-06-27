import os
import fitz            # For reading PDF files
import requests
from dotenv import load_dotenv

# Load our secret token into code
load_dotenv()
TOKEN = os.getenv("HUGGINGFACE_API_KEY")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Choose a Hugging Face model that understands instructions
MODEL_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

# Function to read text from uploaded PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    content = ""
    for page in doc:
        content += page.get_text()
    return content

# Function to ask the AI to classify text
def ask_ai(prompt_text):
    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={"inputs": prompt_text}
    )
    data = response.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "No text found.")
    return "Invalid response format."
# Generates code based on prompt
def generate_code(prompt_text):
    instruction = f"Generate code for the following request:\n\n{prompt_text}"
    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={"inputs": instruction}
    )
    data = response.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "No output.")
    return "Something went wrong with the AI response."
# Fixes bugs in the given code
def fix_buggy_code(code_snippet):
    instruction = (
        "You are a helpful programming assistant. Fix the bugs in the following code "
        "and return the corrected version with no explanation:\n\n"
        f"{code_snippet}"
    )
    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={"inputs": instruction}
    )
    data = response.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "No output.")
    return "Something went wrong with the AI response."
# Generates test cases for the given code
def generate_test_cases(code_snippet):
    prompt = (
        "You are a test engineer. Generate Python unittest test cases "
        "for the following code:\n\n"
        f"{code_snippet}\n\n"
        "Provide only the test code in unittest format."
    )
    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={"inputs": prompt}
    )
    data = response.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "No test cases generated.")
    return "Something went wrong with the AI response."
# Summarizes code logic using Hugging Face model
def summarize_code(code_snippet):
    prompt = (
        "You are a software documentation assistant. Read the following Python code "
        "and summarize what it does in simple language:\n\n"
        f"{code_snippet}\n\n"
        "Your summary should be short, clear, and beginner-friendly."
    )
    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={"inputs": prompt}
    )
    data = response.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "No summary generated.")
    return "Something went wrong with the AI response."
# AI Chatbot for SmartSDLC
def ai_chatbot(user_question):
    prompt = (
        "You are an AI assistant for a software development team. "
        "Answer questions clearly and helpfully. "
        "User asked: " + user_question
    )

    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={"inputs": prompt}
    )

    data = response.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "No response generated.")
    return "Sorry, something went wrong."