import keyboard
import os

# Set working directory to where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Working directory set to: {script_dir}")

import keyboard

# Load macros from a file
def load_macros(file_path):
    macros = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    macros[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return macros

# Function to replace text based on macros
def replace_macros(macros):
    typed_text = ''
    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'space':
                word = typed_text.strip()

                # If the word matches a macro, replace it
                if word in macros:
                    keyboard.write('\b' * (len(word) + 1))  # Delete the typed word and space
                    keyboard.write(macros[word])  # Write the replacement
                
                typed_text = ''  # Reset after space
            elif event.name == 'backspace':
                typed_text = typed_text[:-1]  # Handle backspace
            else:
                typed_text += event.name  # Add the keypress to the typed text

# Main function
def main():
    macro_file = 'macros.txt'  # Path to the user-defined macro file
    macros = load_macros(macro_file)
    
    if macros:
        print("Macro replacement is running. Press ESC to exit.")
        try:
            replace_macros(macros)
        except KeyboardInterrupt:
            print("Exiting...")
    else:
        print("No macros loaded. Exiting...")

if __name__ == '__main__':
    main()
