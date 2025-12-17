import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path="."):
    working_dir_abs = os.path.abspath(working_directory) # Get absolute path of the working directory
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))# Normalize and join paths to get target directory
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs # Check if target_dir is within working_directory

    if not os.path.isdir(working_dir_abs):
        return f'Error: The working directory "{working_dir_abs}" does not exist or is not a directory.'
    
    if not os.path.exists(target_dir) or not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{target_dir}"'
    
    if not valid_target_dir:
        return f'Error: Cannot read "{target_dir}" as it is outside the permitted working directory'
    
    with open(target_dir, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string