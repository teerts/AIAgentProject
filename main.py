import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from functions.get_file_content import schema_get_file_content, get_file_content

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY") 
client = genai.Client(api_key=api_key)

model = 'gemini-2.0-flash-001'
working_directory = "./calculator"

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
        schema_get_file_content,
    ]
)

# Map of function name -> function
function_registry = {
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
    "get_file_content": get_file_content,
}

def call_function(function_call):
    function_name = function_call.name
    args = dict(function_call.args)
    args["working_directory"] = working_directory

    if function_name not in function_registry:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    try:
        function_result = function_registry[function_name](**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": str(e)},
                )
            ],
        )

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: python3 main.py <PromptForAI> [--verbose]")
        sys.exit(1)

    user_prompt = args[0]
    verbose = "--verbose" in args

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    for turn in range(20):
        response = client.models.generate_content(
            model=model,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )

        # Add all candidate messages to the ongoing conversation
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

        if not response.function_calls:
            print("Final response:\n" + response.text)
            break  # LLM is done

        for function_call in response.function_calls:
            print(f"- Calling function: {function_call.name}")

            # Call the function and add result to messages
            content = call_function(function_call)
            messages.append(content)

            # If verbose, show details
            func_response = content.parts[0].function_response.response
            if verbose:
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                print("Function result:")
                print(func_response.get("result", func_response))

    else:
        print("Reached maximum iteration limit (20). Agent may be stuck.")

if __name__ == "__main__":
    main()
