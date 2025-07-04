import os
from google.genai import types

def get_files_info(working_directory, directory=None): 
    full_path = os.path.abspath(os.path.join(working_directory, directory or "")) 

    working_dir_abs = os.path.abspath(working_directory) 
    
    if not full_path.startswith(working_dir_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    items = os.listdir(full_path) 
    lines = []

    for item in items: 
        item_path = os.path.join(full_path, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path) 
        lines.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}') 

    return "\n".join(lines) 

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

