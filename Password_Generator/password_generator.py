import random  # Import the random module for generating random choices
import string  # Import the string module for pre-defined character sets

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    """Generate a random password based on user specifications.

    Args:
        length (int): The desired length of the password.
        use_upper (bool): Whether to include uppercase letters.
        use_lower (bool): Whether to include lowercase letters.
        use_digits (bool): Whether to include digits.
        use_special (bool): Whether to include special characters.

    Returns:
        str: A randomly generated password.

    Raises:
        ValueError: If no character types are selected.
    """
    characters = ""  # Initialize an empty string to hold possible characters
    
    # Add character types based on user choices
    if use_upper:
        characters += string.ascii_uppercase  # Add uppercase letters
    if use_lower:
        characters += string.ascii_lowercase  # Add lowercase letters
    if use_digits:
        characters += string.digits  # Add digits
    if use_special:
        characters += string.punctuation  # Add special characters
    
    # Check if at least one character type was selected
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    # Generate a random password by selecting random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Return the generated password

def main():
    """Main function to run the password generator application."""
    print("Welcome to the Random Password Generator!")  # Greeting the user
    
    try:
        # Prompt the user for password length and character type preferences
        length = int(input("Enter the desired length of the password (e.g., 12): "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate the password based on user inputs
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        
        # Display the generated password to the user
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        # Handle errors (e.g., if no character types were selected)
        print(f"Error: {e}")

if __name__ == "__main__":
    # Entry point for the program
    main()
