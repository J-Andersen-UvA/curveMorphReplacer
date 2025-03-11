"""
replace_curves.py

This script reads the file 'inCurves.txt', replaces all occurrences of a given string 
with another string, and copies the modified text to the clipboard.

Usage:
    python replace_curves.py <split_string> <replace_string>

Example:
    python replace_curves.py glassesGuy mageGuy
    - This replaces all occurrences of "glassesGuy" with "mageGuy" in 'inCurves.txt' 
      and copies the updated content to the clipboard.

Dependencies:
    - Install 'pyperclip' if not already installed:
      pip install pyperclip

"""

import sys
import pyperclip

def replace_text_in_file(file_path, split_string, replace_string):
    """
    Reads the given file, replaces all occurrences of split_string with replace_string,
    and copies the modified text to the clipboard.
    
    :param file_path: Path to the input text file
    :param split_string: The string to be replaced
    :param replace_string: The string to replace with
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        updated_content = content.replace(split_string, replace_string)
        pyperclip.copy(updated_content)
        print("Updated content copied to clipboard.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python replace_curves.py <split_string> <replace_string>")
        sys.exit(1)

    split_string = sys.argv[1]
    replace_string = sys.argv[2]

    replace_text_in_file("inCurves.txt", split_string, replace_string)
