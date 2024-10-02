import tkinter as tk
from tkinter import ttk

# Conversion function to convert any unit to grams
def convert_to_grams(value, unit):
    if unit == 'kg':
        return value * 1000
    elif unit == 'mL':
        return value  # Assuming density of 1g/mL for simplification
    elif unit == 'L':
        return value * 1000
    elif unit == 'cm³':
        return value  # Assuming density of 1g/cm³ for simplification
    return value  # grams

def calculate_cost():
    """
    Fetches user input, calculates the cost of resin needed for the mold,
    and displays the result in the UI.
    """
    try:
        resin_cost_per_unit = float(resin_cost_entry.get())  # Cost of resin
        resin_volume_weight = float(resin_volume_entry.get())  # Volume/Weight of resin
        mold_volume_weight = float(mold_volume_entry.get())  # Volume/Weight of mold

        resin_unit = resin_unit_var.get()  # Selected unit for resin
        mold_unit = mold_unit_var.get()  # Selected unit for mold

        # Convert to grams for consistent calculations
        resin_weight_grams = convert_to_grams(resin_volume_weight, resin_unit)
        mold_weight_grams = convert_to_grams(mold_volume_weight, mold_unit)

        # Calculate total cost
        total_cost = (resin_cost_per_unit / resin_weight_grams) * mold_weight_grams

        # Display the result
        result_label.config(text=f"Total Cost: ${total_cost:.2f}")

    except ValueError:
        result_label.config(text="Error: Please enter valid numeric values.")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Resin Calculator")

# Create and place UI components
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Resin cost label and entry
resin_cost_label = ttk.Label(frame, text="Cost of Resin per Unit:")
resin_cost_label.grid(row=0, column=0, sticky=tk.W)

resin_cost_entry = ttk.Entry(frame, width=10)
resin_cost_entry.grid(row=0, column=1)

# Resin volume/weight label and entry
resin_volume_label = ttk.Label(frame, text="Resin Volume/Weight:")
resin_volume_label.grid(row=1, column=0, sticky=tk.W)

resin_volume_entry = ttk.Entry(frame, width=10)
resin_volume_entry.grid(row=1, column=1)

# Unit options
unit_options = ['g', 'kg', 'mL', 'L', 'cm³']

# Create unit selectors for resin
resin_unit_var = tk.StringVar(value='g')
resin_unit_label = ttk.Label(frame, text="Unit for Resin:")
resin_unit_label.grid(row=0, column=2, sticky=tk.W)
resin_unit_menu = ttk.Combobox(frame, textvariable=resin_unit_var, values=unit_options, state='readonly')
resin_unit_menu.grid(row=0, column=3)

# Mold volume/weight label and entry
mold_volume_label = ttk.Label(frame, text="Mold Volume/Weight:")
mold_volume_label.grid(row=2, column=0, sticky=tk.W)

mold_volume_entry = ttk.Entry(frame, width=10)
mold_volume_entry.grid(row=2, column=1)

# Create unit selectors for mold
mold_unit_var = tk.StringVar(value='g')
mold_unit_label = ttk.Label(frame, text="Unit for Mold:")
mold_unit_label.grid(row=2, column=2, sticky=tk.W)
mold_unit_menu = ttk.Combobox(frame, textvariable=mold_unit_var, values=unit_options, state='readonly')
mold_unit_menu.grid(row=2, column=3)

# Calculate button
calculate_button = ttk.Button(frame, text="Calculate Cost", command=calculate_cost)
calculate_button.grid(row=3, columnspan=4, pady=10)

# Result label to display the result
result_label = ttk.Label(frame, text="", relief="sunken", padding=(10, 10))
result_label.grid(row=4, columnspan=4, sticky=(tk.W, tk.E))

# Start the Tkinter main loop
root.mainloop()