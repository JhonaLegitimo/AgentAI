import os

def write_file(working_directory, file_path, content):
    

    working_dir_abs = os.path.abspath(working_directory)  # Get absolute path of the working directory
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))  # Normalize and join paths to get target file
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs  # Check if target_file is within working_directory

    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # Ensure the directory for the target file exists
    target_dir = os.path.dirname(target_file)
    os.makedirs(target_dir, exist_ok=True)

    with open(target_file, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'