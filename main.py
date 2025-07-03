import os 
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY") 
client = genai.Client(api_key=api_key)

model = 'gemini-2.0-flash-001'
contents = ''

def main():       
    args = sys.argv

    expected_num_args = 2
    if len(sys.argv) < expected_num_args:
        print("Usage: python3 main.py <PromptForAI>")
        sys.exit(1)

    prompt_content_for_ai_arg = 1 
    contents = args[prompt_content_for_ai_arg] 

    response = client.models.generate_content(model=model, contents=contents) 
    
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
