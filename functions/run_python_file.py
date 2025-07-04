import os 
import subprocess 
from google.genai import types

def run_python_file(working_directory, file_path):
    try: 
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        result = subprocess.run(
            ['python3', full_path],
            cwd=working_directory,
            capture_output=True, 
            text=True,
            timeout=30
        )

        output_parts = []

        if result.stdout.strip(): 
            output_parts.append("STDOUT:\n" + result.stdout.strip())

        if result.stderr.strip():
            output_parts.append("STDERR:\n" + result.stderr.strip())

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)

    except Exception as e: 
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file located within the working directory and returns its output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the Python file to execute, from within the working directory. Must end with '.py'."
            ),
        },
        required=["file_path"],
    ),
)
