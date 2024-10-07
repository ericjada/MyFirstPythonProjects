import tkinter as tk
from tkinter import scrolledtext
import ollama
import json
import os

class ChatUI:
    def __init__(self, root):
        self.root = root
        self.model = "llama3.2"  # The model you're using
        self.memory_directory = r'./LLM_Chat'  # Save user memory files here
        os.makedirs(self.memory_directory, exist_ok=True)  # Create the directory if it doesn't exist

        # Set up the UI components
        self.root.title("Chat with Ollama LLM")
        self.root.geometry("600x600")

        # Chat display area (output window)
        self.chat_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # User input field (now a multi-line Text widget)
        self.user_input = tk.Text(self.root, height=5, wrap=tk.WORD)
        self.user_input.pack(pady=10, padx=10, fill=tk.X)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10, padx=10)

        # Load conversation memory for user (hardcoding a user ID for standalone use)
        self.user_id = "default_user"
        self.memory_data = self.load_memory(self.user_id)

        # Display previous conversation in the chat window
        self.display_previous_conversation()

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

    def display_previous_conversation(self):
        """Displays the loaded conversation history in the chat window."""
        self.chat_window.config(state=tk.NORMAL)
        for message in self.memory_data['history']:
            if message['role'] == 'user':
                self.chat_window.insert(tk.END, "You: " + message['content'] + "\n")
            elif message['role'] == 'assistant':
                self.chat_window.insert(tk.END, "LLM: " + message['content'] + "\n")
        self.chat_window.config(state=tk.DISABLED)

    def send_message(self):
        user_message = self.user_input.get("1.0", tk.END).strip()  # Get all text from the Text widget
        if user_message:
            self.chat_window.config(state=tk.NORMAL)
            self.chat_window.insert(tk.END, "You: " + user_message + "\n")
            self.chat_window.config(state=tk.DISABLED)

            # Add the user prompt to the conversation history
            self.memory_data['history'].append({'role': 'user', 'content': user_message})

            # Call Ollama API with conversation history
            self.chat_window.config(state=tk.NORMAL)
            self.chat_window.insert(tk.END, "🤔 I'm thinking... Please hold on!\n")
            self.chat_window.config(state=tk.DISABLED)
            self.root.update_idletasks()  # Update the UI before sending the request

            try:
                # Prepare the conversation history
                messages = self.memory_data['history'].copy()

                # Using Ollama to generate a response
                response = ollama.chat(model=self.model, messages=messages)
                print("Ollama response:", response)  # Debugging purposes

                # Extract the content from the response
                bot_response = response['message']['content']

                # Display the response
                self.chat_window.config(state=tk.NORMAL)
                self.chat_window.insert(tk.END, "LLM: " + bot_response + "\n")
                self.chat_window.config(state=tk.DISABLED)

                # Add the bot's response to the conversation history
                self.memory_data['history'].append({'role': 'assistant', 'content': bot_response})

                # Save the updated conversation history
                self.save_memory(self.user_id, self.memory_data)

            except Exception as e:
                self.chat_window.config(state=tk.NORMAL)
                self.chat_window.insert(tk.END, f'Error: {str(e)}\n')
                self.chat_window.config(state=tk.DISABLED)

            # Clear input field
            self.user_input.delete("1.0", tk.END)

# Initialize Tkinter window and run the chat UI
root = tk.Tk()
chat_ui = ChatUI(root)
root.mainloop()
