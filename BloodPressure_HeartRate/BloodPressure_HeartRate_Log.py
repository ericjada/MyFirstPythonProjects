import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import os
import subprocess

# File path using relative path ./ (current directory)
file_path = './BloodPressure_HeartRate_Log.xlsx'

def save_entry():
    systolic = int(entry_systolic.get())
    diastolic = int(entry_diastolic.get())
    heart_rate = int(entry_heartrate.get())
    
    # Get the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Determine blood pressure feedback
    if systolic < 120 and diastolic < 80:
        bp_status = "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        bp_status = "Elevated"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        bp_status = "Stage 1 Hypertension"
    elif systolic >= 140 or diastolic >= 90:
        bp_status = "Stage 2 Hypertension"
    else:
        bp_status = "Unknown"

    # Determine heart rate feedback
    if 60 <= heart_rate <= 70:
        hr_status = "Normal"
    elif 70 < heart_rate <= 80:
        hr_status = "Slightly above normal"
    elif 80 < heart_rate <= 90:
        hr_status = "Above normal"
    elif 90 < heart_rate <= 100:
        hr_status = "Elevated heart rate"
    else:
        hr_status = "Unknown"

    # Create a DataFrame for the entry
    entry_data = pd.DataFrame({
        'Date/Time': [date_time],
        'Systolic': [systolic],
        'Diastolic': [diastolic],
        'Heart Rate': [heart_rate],
        'BP Status': [bp_status],
        'HR Status': [hr_status]
    })

    # Save to Excel file (append if file exists)
    if os.path.exists(file_path):
        entry_data.to_excel(file_path, index=False, header=False, mode='a')
    else:
        entry_data.to_excel(file_path, index=False)

    # Provide feedback to user
    messagebox.showinfo("Entry Submitted", 
                        f"Your entry has been saved.\n"
                        f"Blood Pressure: {bp_status}\n"
                        f"Heart Rate: {hr_status}")

def open_file():
    if os.path.exists(file_path):
        subprocess.Popen(["start", file_path], shell=True)  # Use subprocess to open the file
    else:
        messagebox.showerror("Error", "File not found!")

# Set up the GUI
root = tk.Tk()
root.title("Blood Pressure & Heart Rate Log")

# Systolic input
tk.Label(root, text="Systolic (mm Hg):").grid(row=0, column=0, padx=10, pady=5)
entry_systolic = tk.Entry(root)
entry_systolic.grid(row=0, column=1, padx=10, pady=5)

# Diastolic input
tk.Label(root, text="Diastolic (mm Hg):").grid(row=1, column=0, padx=10, pady=5)
entry_diastolic = tk.Entry(root)
entry_diastolic.grid(row=1, column=1, padx=10, pady=5)

# Heart rate input
tk.Label(root, text="Heart Rate (bpm):").grid(row=2, column=0, padx=10, pady=5)
entry_heartrate = tk.Entry(root)
entry_heartrate.grid(row=2, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=save_entry)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Open file button
open_button = tk.Button(root, text="Open Log File", command=open_file)
open_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
