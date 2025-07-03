import os 

def get_file_content(working_directory, file_path): 
    try: 
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory) 

        if not full_path.startswith(working_directory_abs): 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 

        if not os.path.isfile(full_path): 
            return f'Error: File not found or is not a regular file: "{file_path}"' 

        max_content_length = 10000
        with open(full_path, 'r') as file: 
            content = file.read() 
            if len(content) > max_content_length: 
                return content[:max_content_length] + f'\n[...File "{file_path}" truncated at {max_content_length} characters]'
            return content 

    except Exception as e: 
        return f'Error: {str(e)}'
