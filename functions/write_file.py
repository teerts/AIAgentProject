import os
from google.genai import types

def write_file(working_directory, file_path, content): 
    try: 
        full_path = os.path.abspath(os.path.join(working_directory, file_path)) 
        working_directory_abs = os.path.abspath(working_directory) 

        if not full_path.startswith(working_directory_abs): 
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 

        os.makedirs(os.path.dirname(full_path), exist_ok=True) 

        with open(full_path, 'w') as f: 
            f.write(content) 

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
    
    except Exception as e: 
        return f'Error: {str(e)}' 
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist and overwrites existing content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to write to, from within the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file."
            ),
        },
        required=["file_path", "content"],
    ),
)
