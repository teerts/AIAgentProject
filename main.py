import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_file_content import schema_get_file_content

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY") 
client = genai.Client(api_key=api_key)

model = 'gemini-2.0-flash-001'
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_run_python_file,
        schema_write_file,
        schema_get_file_content
    ]
)

def main():       
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: python3 main.py <PromptForAI> [--verbose]")
        sys.exit(1)
    
    contents = args[0] 

    messages = [types.Content(role="user", parts=[types.Part(text=contents)])]
    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))    
    
    if len(response.function_calls) == 0:
        print(response.text)
    else:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")

    verbose = "--verbose" in args

    if verbose:
        print(f"User prompt: {contents}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
