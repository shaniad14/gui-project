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