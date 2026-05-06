import tkinter as tk

# create window
root = tk.Tk()
root.title("BMI App")

# FRAME
frame = tk.Frame(root)
frame.pack()

# MASS
l1 = tk.Label(frame, text="Mass (kg):")
l1.grid(row=0, column=0)

e1 = tk.Entry(frame)
e1.grid(row=0, column=1)

#  HEIGHT
l2 = tk.Label(frame, text="Height (m):")
l2.grid(row=1, column=0)

e2 = tk.Entry(frame)
e2.grid(row=1, column=1)

#  CHECKBUTTON 
a = tk.IntVar()
c1 = tk.Checkbutton(frame, text="Athlete", variable=a)
c1.grid(row=2, column=0, columnspan=2)

#  LABEL
l3 = tk.Label(frame, text="BMI: ")
l3.grid(row=4, column=0, columnspan=2)

#  CANVAS 
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# draw a rectangle 
canvas.create_rectangle(50, 25, 150, 75)

#  FUNCTION 
def calc():
    m = float(e1.get())
    h = float(e2.get())

    bmi = round(m / (h * h), 2)

    text = "BMI: " + str(bmi)

    if a.get() == 1:
        text += " (Athlete)"

    l3["text"] = text

#  BUTTON 
b1 = tk.Button(frame, text="Calculate BMI", command=calc)
b1.grid(row=3, column=0, columnspan=2)

# run app
root.mainloop()



