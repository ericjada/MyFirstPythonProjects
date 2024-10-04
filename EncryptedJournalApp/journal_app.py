import os
from tkinter import *
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
from datetime import datetime

# Helper function to derive key from the passphrase
def derive_key(phrase):
    salt = b'salt_' + phrase.encode()  # Use a static salt based on the phrase (simple for demo)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(phrase.encode()))
    return Fernet(key)

def encrypt_message(message, key):
    return key.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    return key.decrypt(encrypted_message).decode()

# File handling and user management
def save_journal_entry(username, key_phrase, entry):
    # Create user folder if it doesn't exist
    folder_path = f"./journals/{username}"
    os.makedirs(folder_path, exist_ok=True)

    # Derive key from the passphrase
    key = derive_key(key_phrase)
    encrypted_entry = encrypt_message(entry, key)

    # Save to a .txt file with date in the filename
    filename = f"{folder_path}/journal_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, 'wb') as f:
        f.write(encrypted_entry)

    messagebox.showinfo("Success", "Journal entry saved!")

def load_journal_entry(username, file_path, key_phrase):
    # Read the encrypted journal entry
    with open(file_path, 'rb') as f:
        encrypted_entry = f.read()

    # Derive key from the passphrase
    key = derive_key(key_phrase)
    try:
        decrypted_entry = decrypt_message(encrypted_entry, key)
        return decrypted_entry
    except Exception:
        messagebox.showerror("Error", "Incorrect key phrase")
        return None

# UI
class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encrypted Journal")

        self.username = StringVar()
        self.key_phrase = StringVar()

        # Login Frame
        self.login_frame = Frame(self.root)
        self.login_frame.pack(pady=10)

        # Make the Entry fields wider
        Label(self.login_frame, text="Username:").pack()
        Entry(self.login_frame, textvariable=self.username, width=60).pack()  # Adjusted width

        Label(self.login_frame, text="Key Phrase:").pack()
        Entry(self.login_frame, textvariable=self.key_phrase, show="*", width=60).pack()  # Adjusted width

        Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        Button(self.login_frame, text="New User", command=self.new_user).pack(pady=10)

    def login(self):
        username = self.username.get()
        key_phrase = self.key_phrase.get()

        if not username or not key_phrase:
            messagebox.showerror("Error", "Please provide both username and key phrase")
            return

        # Check if user exists
        if not os.path.exists(f"./journals/{username}"):
            messagebox.showerror("Error", "User does not exist, please create a new account")
            return

        # Transition to the journal entry screen
        self.login_frame.pack_forget()
        self.main_interface(username, key_phrase)

    def new_user(self):
        username = self.username.get()
        key_phrase = self.key_phrase.get()

        if not username or not key_phrase:
            messagebox.showerror("Error", "Please provide both username and key phrase")
            return

        # Check if username already exists
        if os.path.exists(f"./journals/{username}"):
            messagebox.showerror("Error", "Username already exists, please choose a different one")
        else:
            os.makedirs(f"./journals/{username}")
            messagebox.showinfo("Success", f"User '{username}' created!")
    
    def main_interface(self, username, key_phrase):
        self.username = username
        self.key_phrase = key_phrase

        # Main Journal Interface
        self.main_frame = Frame(self.root)
        self.main_frame.pack(pady=10)

        # Journal Entry Text Box
        self.entry_box = Text(self.main_frame, height=10, width=50)
        self.entry_box.pack()

        # Submit button
        Button(self.main_frame, text="Submit", command=self.submit_entry).pack(pady=5)

        # File List and Decryption area
        # Make the Listbox wider
        self.file_list_box = Listbox(self.main_frame, width=60)  # Adjusted width for file list
        self.file_list_box.pack(pady=10)
        self.load_files()

        self.decrypted_text = Text(self.main_frame, height=10, width=60)  # Adjusted width for decrypted text
        self.decrypted_text.pack()

        Button(self.main_frame, text="Read Selected Entry", command=self.read_entry).pack(pady=5)

    def load_files(self):
        folder_path = f"./journals/{self.username}"
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in files:
                self.file_list_box.insert(END, file)

    def submit_entry(self):
        entry = self.entry_box.get("1.0", END).strip()
        if entry:
            save_journal_entry(self.username, self.key_phrase, entry)
            self.entry_box.delete("1.0", END)
            self.file_list_box.delete(0, END)
            self.load_files()
        else:
            messagebox.showerror("Error", "Journal entry cannot be empty")

    def read_entry(self):
        selected_file = self.file_list_box.get(ACTIVE)
        if selected_file:
            file_path = f"./journals/{self.username}/{selected_file}"
            decrypted_entry = load_journal_entry(self.username, file_path, self.key_phrase)
            if decrypted_entry:
                self.decrypted_text.delete("1.0", END)
                self.decrypted_text.insert(END, decrypted_entry)
        else:
            messagebox.showerror("Error", "Please select a file to read")


# Main program execution
if __name__ == "__main__":
    root = Tk()
    app = JournalApp(root)
    root.mainloop()
