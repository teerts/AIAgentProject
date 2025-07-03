import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY") 
client = genai.Client(api_key=api_key)

model = 'gemini-2.0-flash-001'

def main():       
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: python3 main.py <PromptForAI> [--verbose]")
        sys.exit(1)

    prompt_content_for_ai_arg = 1 
    contents = args[0] 

    messages = [types.Content(role="user", parts=[types.Part(text=contents)])]
    response = client.models.generate_content(model=model, contents=messages)    
    print(response.text)

    verbose = "--verbose" in args

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
