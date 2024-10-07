import tkinter as tk
from tkinter import scrolledtext
import ollama
import json
import os

class ChatUI:
    def __init__(self, root):
        self.root = root
        self.model = "llama3.2"  # The model you're using
        self.memory_directory = r'C:\Users\ericj\Documents\GitHub\MyFirstPythonProject\LLM_Chat'  # Save user memory files here
        self.files_directory = r'C:\Users\ericj\Documents\GitHub\MyFirstPythonProject\LLM_Chat\files'  # Directory for .txt files
        os.makedirs(self.memory_directory, exist_ok=True)  # Create the directory if it doesn't exist

        # Set up the UI components
        self.root.title("Chat with Ollama LLM")
        self.root.geometry("600x600")

        # Create a frame to hold the canvas and the scrollbar
        self.frame = tk.Frame(self.root)
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

    def display_previous_conversation(self):
        """Displays the loaded conversation history in the chat window."""
        for message in self.memory_data['history']:
            if message['role'] == 'user':
                self.display_bubble("You", message['content'], "lightblue")
            elif message['role'] == 'assistant':
                self.display_bubble("LLM", message['content'], "lightgreen")
        self.scroll_to_bottom()

    def display_bubble(self, sender, message, color):
        """Displays a message bubble in the chat."""
        bubble = tk.Frame(self.chat_frame, bg=color, relief="flat", bd=5)

        # Adjust label to allow left alignment for multi-line text
        label = tk.Label(bubble, text=f"{sender}: {message}", bg=color, padx=10, pady=5, 
                         wraplength=500, justify="left", anchor="w")  

        label.pack(fill='x')

        # Add the bubble to the frame
        bubble.pack(fill='x', padx=5, pady=5)

        # Scroll to the bottom after displaying a new bubble
        self.scroll_to_bottom()

    def combine_with_file_contents(self, messages):
        """Combines the conversation history with contents of all .txt files."""
        combined_prompt = messages.copy()
        
        # Read all .txt files in the specified directory
        for filename in os.listdir(self.files_directory):
            if filename.endswith('.txt'):
                with open(os.path.join(self.files_directory, filename), 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    combined_prompt.append({'role': 'system', 'content': file_contents})  # Combine with the conversation messages

        return combined_prompt

    def send_message(self):
        user_message = self.user_input.get("1.0", tk.END).strip()
        if user_message:
            self.display_bubble("You", user_message, "lightblue")

            # Add the user prompt to the conversation history
            self.memory_data['history'].append({'role': 'user', 'content': user_message})

            self.display_bubble("LLM", "🤔 I'm thinking... Please hold on!", "lightgreen")
            self.root.update_idletasks()

            try:
                messages = self.memory_data['history'].copy()
                combined_prompt = self.combine_with_file_contents(messages)

                # Using Ollama to generate a streaming response
                stream = ollama.chat(model=self.model, messages=combined_prompt, stream=True)
                for chunk in stream:
                    # Display each chunk of the response as it is received
                    self.display_bubble("LLM", chunk['message']['content'], "lightgreen")
                    self.root.update_idletasks()  # Keep the UI responsive

                # After streaming, save the updated conversation history
                self.save_memory(self.user_id, self.memory_data)

            except Exception as e:
                self.display_bubble("Error", str(e), "red")

            # Clear input field
            self.user_input.delete("1.0", tk.END)

    def on_frame_configure(self, event):
        """Update the scroll region of the canvas to encompass the frame."""
        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

    def scroll_to_bottom(self):
        """Scrolls the chat canvas to the bottom."""
        self.chat_canvas.yview_moveto(1.0)

# Initialize Tkinter window and run the chat UI
if __name__ == "__main__":
    root = tk.Tk()
    chat_ui = ChatUI(root)
    root.mainloop()
