import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)  # Get absolute path of the working directory
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))  # Normalize and join paths to get target file
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs  # Check if target_file is within working_directory

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file) or not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file]
    if args:
        command.extend(args)
    
    try:
        output_parts = []
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not result.stdout.strip() and not result.stderr.strip():
            output_parts.append("No output produced")
        else:
            if result.stdout.strip():
                output_parts.append(f"STDOUT:\n{result.stdout}")
            
            if result.stderr.strip():
                output_parts.append(f"STDERR:\n{result.stderr}")
        return "\n".join(output_parts)
    
    except subprocess.CalledProcessError as e:
        return f'Error executing Python File: {e.stderr}'
    
    except subprocess.TimeoutExpired as e:
        return f"Process timed out after 30 seconds. Partial STDOUT: {e.stdout}"

print(run_python_file("calculator", "main.py"))