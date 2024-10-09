import tkinter as tk
from tkinter import scrolledtext
import ollama
import json
import os
from datetime import datetime
import threading
import random

class ChatUI:
    def __init__(self, root):
        self.root = root
        self.model = "llama3.2"  # The model you're using
        self.memory_directory = r'C:\Users\ericj\Documents\GitHub\MyFirstPythonProject\LLM_Chat'  # Save user memory files here
        self.files_directory = r'C:\Users\ericj\Documents\GitHub\MyFirstPythonProject\LLM_Chat\files'  # Directory for .txt files
        os.makedirs(self.memory_directory, exist_ok=True)  # Create the directory if it doesn't exist

        # Load user preferences
        self.user_preferences = self.load_user_preferences()
        self.font_size = self.user_preferences.get('font_size', 12)

        # Set up the UI components
        self.root.title("Chat with Ollama LLM")
        self.root.geometry("600x600")
        self.root.config(bg="#f7f7f7")

        # Create a frame to hold the canvas and the scrollbar
        self.frame = tk.Frame(self.root, bg="#f7f7f7")
        self.frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Chat display area (Canvas for message bubbles)
        self.chat_canvas = tk.Canvas(self.frame, bg="white")
        self.chat_scrollbar = tk.Scrollbar(self.frame, command=self.chat_canvas.yview)
        self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)

        self.chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a frame to contain chat bubbles
        self.chat_frame = tk.Frame(self.chat_canvas, bg="white")
        self.chat_canvas.create_window((0, 0), window=self.chat_frame, anchor='nw')

        # User input field (now a multi-line Text widget)
        self.user_input = tk.Text(self.root, height=5, wrap=tk.WORD, bg="#f0f0f0", font=("Arial", self.font_size), padx=10, pady=10)
        self.user_input.pack(pady=10, padx=10, fill=tk.X)
        self.user_input.insert(tk.END, "Type your message here...")  # Placeholder text
        self.user_input.bind("<FocusIn>", self.clear_placeholder)  # Clear placeholder on focus
        self.user_input.bind("<FocusOut>", self.set_placeholder)  # Set placeholder if empty
        self.user_input.bind("<KeyRelease>", self.auto_resize_input)  # Auto resize on key release

        # Character counter
        self.char_counter = tk.Label(self.root, text=f"Characters left: {200}", font=("Arial", 10), bg="#f7f7f7")
        self.char_counter.pack(pady=(0, 5))
        self.user_input.bind("<KeyRelease>", self.update_char_counter)

        # Emoji button
        self.emoji_button = tk.Button(self.root, text="😀", command=self.insert_emoji, font=("Arial", 14))
        self.emoji_button.pack(side=tk.LEFT, padx=10)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.send_button.pack(pady=10, padx=10)

        # Load conversation memory for user (hardcoding a user ID for standalone use)
        self.user_id = "default_user"
        self.memory_data = self.load_memory(self.user_id)

        # User and assistant names configuration
        self.user_name = "You"  # Change this to set a custom name
        self.assistant_name = "LLM"  # Change this to set a custom name

        # Display previous conversation in the chat window
        self.display_previous_conversation()

        # Bind Enter key to send message
        self.user_input.bind("<Return>", lambda event: self.send_message())

        # Update the scroll region of the canvas
        self.chat_frame.bind("<Configure>", self.on_frame_configure)

        # Scroll to the bottom on startup
        self.scroll_to_bottom()

    def load_memory(self, user_id):
        """Loads the conversation history from a user's file."""
        memory_file = os.path.join(self.memory_directory, f'{user_id}.json')
        if os.path.exists(memory_file):
            with open(memory_file, 'r') as file:
                return json.load(file)
        return {'name': '', 'history': []}  # Return empty history if no file exists

    def save_memory(self, user_id, memory_data):
        """Saves the conversation history to a user's file."""
        memory_file = os.path.join(self.memory_directory, f'{user_id}.json')
        with open(memory_file, 'w') as file:
            json.dump(memory_data, file)

    def load_user_preferences(self):
        """Loads user preferences from a JSON file."""
        preferences_file = os.path.join(self.memory_directory, 'preferences.json')
        if os.path.exists(preferences_file):
            with open(preferences_file, 'r') as file:
                return json.load(file)
        return {'font_size': 12}  # Default preferences

    def save_user_preferences(self):
        """Saves user preferences to a JSON file."""
        preferences_file = os.path.join(self.memory_directory, 'preferences.json')
        preferences = {'font_size': self.font_size}
        with open(preferences_file, 'w') as file:
            json.dump(preferences, file)

    def display_previous_conversation(self):
        """Displays the loaded conversation history in the chat window."""
        for message in self.memory_data['history']:
            sender = self.user_name if message['role'] == 'user' else self.assistant_name
            color = "lightblue" if message['role'] == 'user' else "lightgreen"
            self.display_bubble(sender, message['content'], color)
        self.scroll_to_bottom()

    def display_bubble(self, sender, message, color):
        """Displays a message bubble in the chat."""
        bubble = tk.Frame(self.chat_frame, bg=color, relief="flat", bd=5, padx=5, pady=5, highlightbackground="gray", highlightcolor="gray")

        # Add timestamp to message
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"{message} \n\n <{timestamp}>"

        # Adjust label to allow left alignment for multi-line text
        label = tk.Label(bubble, text=f"{sender}: {formatted_message}", bg=color, padx=10, pady=5, 
                         wraplength=500, justify="left", anchor="w", font=("Arial", self.font_size))

        label.pack(fill='x')

        # Add the bubble to the frame
        bubble.pack(fill='x', padx=5, pady=5)

        return bubble  # Return the bubble frame for further reference

    def send_message(self):
        """Handles sending the user's message to the model."""
        user_message = self.user_input.get("1.0", tk.END).strip()
        if user_message == "" or user_message == "Type your message here...":
            return  # Prevent sending empty messages

        # Display the user message bubble
        self.display_bubble(self.user_name, user_message, "lightblue")
        self.user_input.delete("1.0", tk.END)  # Clear input field
        self.scroll_to_bottom()  # Scroll to the bottom

        # Display loading bubble
        loading_bubble = self.display_bubble("Loading...", "", "lightyellow")
        self.root.update_idletasks()  # Update the UI

        # Process the message in a new thread
        threading.Thread(target=self.process_message, args=(user_message, loading_bubble)).start()

    def combine_with_file_contents(self, messages):
        """Combines the existing conversation with the content of text files."""
        combined_prompt = messages.copy()  # Copy existing messages

        # Load content from .txt files in the specified directory
        for filename in os.listdir(self.files_directory):
            if filename.endswith('.txt'):
                with open(os.path.join(self.files_directory, filename), 'r') as file:
                    file_content = file.read()
                    combined_prompt.append({'role': 'user', 'content': file_content})  # Append as user input

        return combined_prompt

    def process_message(self, user_message, loading_bubble):
        """Handles the processing of the user's message and getting a response from the model."""
        try:
            messages = self.memory_data['history'].copy()
            combined_prompt = self.combine_with_file_contents(messages)

            # Using Ollama to generate a streaming response
            stream = ollama.chat(model=self.model, messages=combined_prompt, stream=True)
            response_content = ""

            for chunk in stream:
                # Append each chunk of the response
                response_content += chunk['message']['content']
                # Update the loading bubble with the latest response
                loading_bubble.pack_forget()  # Remove loading bubble before displaying the response
                self.display_bubble(self.assistant_name, response_content, "lightgreen")
                self.root.update_idletasks()  # Keep the UI responsive

            # After streaming, save the updated conversation history
            self.memory_data['history'].append({'role': 'assistant', 'content': response_content})
            self.save_memory(self.user_id, self.memory_data)

        except Exception as e:
            self.display_bubble("Error", str(e), "red")

    def insert_emoji(self):
        """Inserts a random emoji into the input field."""
        emojis = ['😀', '😄', '😁', '😆', '😅', '😂', '😊', '😍', '😎', '😏']
        self.user_input.insert(tk.END, random.choice(emojis))

    def update_char_counter(self, event=None):
        """Updates the character counter based on the user input."""
        current_length = len(self.user_input.get("1.0", tk.END)) - 1  # Exclude the last newline
        characters_left = max(0, 200 - current_length)
        self.char_counter.config(text=f"Characters left: {characters_left}")

    def on_frame_configure(self, event):
        """Update the scroll region of the canvas to encompass the frame."""
        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

    def scroll_to_bottom(self):
        """Scrolls the chat canvas to the bottom."""
        self.chat_canvas.yview_moveto(1.0)

    def clear_placeholder(self, event):
        """Clears the placeholder text when the input field is focused."""
        if self.user_input.get("1.0", tk.END).strip() == "Type your message here...":
            self.user_input.delete("1.0", tk.END)

    def set_placeholder(self, event):
        """Sets the placeholder text if the input field is empty."""
        if self.user_input.get("1.0", tk.END).strip() == "":
            self.user_input.insert(tk.END, "Type your message here...")

    def auto_resize_input(self, event):
        """Automatically resize the input field based on user input."""
        current_height = self.user_input.index('end-1c').count('\n') + 1  # Count lines
        self.user_input.config(height=current_height)

# Initialize Tkinter window and run the chat UI
if __name__ == "__main__":
    root = tk.Tk()
    chat_ui = ChatUI(root)
    root.mainloop()
