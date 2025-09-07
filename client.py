import requests
import json
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

def get_gemini_response(user_input):
    # Get the API key from the environment variable
    API_KEY = os.getenv("API_KEY")
    
    if not API_KEY:
        return "Error: API_KEY environment variable not set."
    
    # The API endpoint for the Gemini Flash 2.0 model
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={API_KEY}"
    
    # System instruction
    system_instruction = "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Since you are a voice assistant, try to answer under 30 words and without special characters, and in a single paragraph without bullet points."
    
    # User prompt
    user_prompt = f"{user_input}"
    
    # The payload for the API request
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": user_prompt}]}
        ],
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        }
    }
    
    # Set the headers for the request
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        # Make the POST request to the Gemini API
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        
        # Parse the JSON response
        response_data = response.json()
        
        # Extract the generated text from the response
        generated_text = response_data['candidates'][0]['content']['parts'][0]['text']
        
        return generated_text
        
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# For standalone testing
if __name__ == "__main__":
    user_word = "What is the weather like today?"  # Example
    result = get_gemini_response(user_word)
    print(result)
