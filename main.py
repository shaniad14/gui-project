"""
BMI calculator GUI
"""

import tkinter as tk

# Set up window
root = tk.Tk()
root.title("BMI Calculator")

# Function to calculate BMI
def calculate_bmi():
    mass = float(entry_mass.get())
    height = scale_height.get()
    
    bmi = round(mass / (height ** 2), 2)
    
    result = f"BMI: {bmi}"

     # Add gender
    result += f" | Gender: {gender.get()}"
    
    # Check athlete box
    if athlete.get() == 1:
        result += " | Athlete"
    
    label_result.config(text=result)

    # Mass input
tk.Label(root, text="Mass (kg):").grid(row=0, column=0)
entry_mass = tk.Entry(root)
entry_mass.grid(row=0, column=1)

# Height slider
scale_height = tk.Scale(root, from_=1.0, to=2.5, resolution=0.01,
                        orient="horizontal", label="Height (m)")
scale_height.grid(row=1, column=0, columnspan=2)

