import os

def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_to_read = os.path.join(script_dir, 'my_file.txt')

read_and_print_file(file_to_read)
