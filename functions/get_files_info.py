import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory) # Get absolute path of the working directory
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))# Normalize and join paths to get target directory
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs # Check if target_dir is within working_directory

    if not os.path.isdir(working_dir_abs):
        return f'Error: The working directory "{working_dir_abs}" does not exist or is not a directory.'
    
    if not os.path.exists(target_dir):
        return f'Error: The directory "{directory}" does not exist.'
    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    list_of_files = os.listdir(target_dir) # List files in the target directory
    if directory == ".":
        name_dir = "current"
    else:
        name_dir = f"'{directory}'"
    result = f"Results for {name_dir} directory"
    for file in list_of_files:
        result += f"\n- {file}: file_size={os.path.getsize(os.path.join(target_dir, file))}, is_dir={os.path.isdir(os.path.join(target_dir, file))}"
    return result