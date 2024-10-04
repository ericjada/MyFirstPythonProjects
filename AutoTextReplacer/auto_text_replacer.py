import os
import threading
import tkinter as tk
import keyboard
import subprocess
import sys

# Set working directory to where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Working directory set to: {script_dir}")

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
    while not stop_event.is_set():
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'space':
                word = typed_text.strip()
                if word in macros:
                    keyboard.write('\b' * (len(word) + 1))  # Delete the typed word and space
                    keyboard.write(macros[word])  # Write the replacement
                typed_text = ''  # Reset after space
            elif event.name == 'backspace':
                typed_text = typed_text[:-1]  # Handle backspace
            else:
                typed_text += event.name  # Add the keypress to the typed text

# Start the macro replacement in a separate thread
def start_macro_replacement():
    macro_file = 'macros.txt'  # Path to the user-defined macro file
    macros = load_macros(macro_file)
    if macros:
        print("Macro replacement is running.")
        replace_macros(macros)
    else:
        print("No macros loaded. Exiting...")

# Function to open the macros.txt file for editing
def open_macros_file():
    try:
        if sys.platform.startswith('win32'):
            subprocess.Popen(['notepad.exe', 'macros.txt'])
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', 'macros.txt'])
        else:
            subprocess.Popen(['xdg-open', 'macros.txt'])
    except Exception as e:
        print(f"Failed to open file: {e}")

# Function to close the UI and stop the macro replacement
def on_closing():
    stop_event.set()  # Signal the replacement thread to stop
    root.destroy()

# Create a thread event to stop the macro replacement
stop_event = threading.Event()

# Create the main application window
root = tk.Tk()
root.title("Auto Text Replacer")

# Create and place a button to open macros.txt
open_button = tk.Button(root, text="Edit Macros", command=open_macros_file)
open_button.pack(pady=20)

# Set the window closing behavior
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the macro replacement thread
threading.Thread(target=start_macro_replacement, daemon=True).start()

# Start the tkinter event loop
root.mainloop()
