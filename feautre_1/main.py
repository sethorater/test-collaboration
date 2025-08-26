import os

# Function to read a file and print its contents
def read_and_print_file(file_path):
    """
    Reads a text file from the given path and prints its content.

    Args:
        file_path (str): The path to the text file.
    """
    try:
        # 'with' statement ensures the file is automatically closed
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            # Print the content
            print(content)
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        # Handle other potential errors during file handling
        print(f"An error occurred: {e}")

# --- NEW CODE TO FIX FILE NOT FOUND ERROR ---
# Get the directory of the current script.
# This ensures the program looks for the file in the same folder as the script itself.
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file.
file_to_read = os.path.join(script_dir, 'my_file.txt')
# --------------------------------------------

read_and_print_file(file_to_read)
