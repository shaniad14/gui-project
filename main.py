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

    # mass
l1 = tk.Label(root, text="Mass")
l1.grid(row=0, column=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)

# height slider
s1 = tk.Scale(root, from_=1.0, to=2.5, resolution=0.1,
              orient="horizontal", label="Height")
s1.grid(row=1, column=0, columnspan=2)


