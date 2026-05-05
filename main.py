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

# gender
g = tk.StringVar()
r1 = tk.Radiobutton(root, text="Male", variable=g, value="Male")
r1.grid(row=2, column=0)

r2 = tk.Radiobutton(root, text="Female", variable=g, value="Female")
r2.grid(row=2, column=1)

# athlete
a = tk.IntVar()
c1 = tk.Checkbutton(root, text="Athlete", variable=a)
c1.grid(row=3, column=0)

# button
b1 = tk.Button(root, text="Calc", command=calc)
b1.grid(row=4, column=0, columnspan=2)

# result
l3 = tk.Label(root, text="BMI:")
l3.grid(row=5, column=0, columnspan=2)

root.mainloop()



