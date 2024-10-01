import tkinter as tk
from tkinter import ttk
import random

def roll_dice(sides, num_rolls=1):
    """
    Rolls a dice with a specified number of sides.
    
    :param sides: Number of sides on the dice.
    :param num_rolls: Number of times to roll the dice.
    :return: A list of results for each roll.
    """
    return [random.randint(1, sides) for _ in range(num_rolls)]  # Roll the dice

def perform_roll():
    """
    Fetches the user input, rolls the dice, and displays the result in the UI.
    """
    try:
        num_rolls = int(num_dice_entry.get())  # Get the number of dice from the user input
        sides = int(dice_type_entry.get())     # Get the number of sides from the user input

        if num_rolls <= 0 or sides <= 0:
            raise ValueError("Values must be positive.")

        # Roll the dice
        rolls = roll_dice(sides, num_rolls)
        total = sum(rolls)  # Calculate the total
        
        # Display the results
        result_label.config(text=f"Rolls: {', '.join(map(str, rolls))}\nTotal: {total}")
    
    except ValueError as e:
        result_label.config(text=f"Error: {e}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("D&D Dice Roller")

# Create and place UI components
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dice type label and entry
dice_type_label = ttk.Label(frame, text="Dice Type (e.g., 6 for a d6):")
dice_type_label.grid(row=0, column=0, sticky=tk.W)

dice_type_entry = ttk.Entry(frame, width=10)
dice_type_entry.grid(row=0, column=1)
dice_type_entry.insert(0, "20")  # Default to d20

# Number of dice label and entry
num_dice_label = ttk.Label(frame, text="Number of Dice:")
num_dice_label.grid(row=1, column=0, sticky=tk.W)

num_dice_entry = ttk.Entry(frame, width=10)
num_dice_entry.grid(row=1, column=1)
num_dice_entry.insert(0, "1")  # Default to 1 dice

# Roll button
roll_button = ttk.Button(frame, text="Roll!", command=perform_roll)
roll_button.grid(row=2, columnspan=2, pady=10)

# Result label to display the result
result_label = ttk.Label(frame, text="", relief="sunken", padding=(10, 10))
result_label.grid(row=3, columnspan=2, sticky=(tk.W, tk.E))

# Start the Tkinter main loop
root.mainloop()
