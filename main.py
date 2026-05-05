import tkinter as tk

root = tk.Tk()
root.title("BMI")

def calc():
    m = float(e1.get())
    h = s1.get()
    
    bmi = round(m / (h*h), 2)
    
    text = "BMI: " + str(bmi)
    
    if g.get() == "Male":
        text += " Male"
    if g.get() == "Female":
        text += " Female"
        
    if a.get() == 1:
        text += " Athlete"
    
    l3["text"] = text


