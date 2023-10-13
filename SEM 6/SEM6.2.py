from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        h = float(height.get())
        m = float(mass.get())
        bmi.set(round(m/(h/100)**2,2))
        if float(bmi.get()) < 25:
            diagnos.set('Normal')
        elif 25 <= float(bmi.get()) <= 29:
            diagnos.set('Overweight')
        elif 29 < float(bmi.get()):
            diagnos.set('Obese')
    except ValueError:
        pass
root = Tk()

root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=1, row=1, sticky=(W, E))

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=1, row=2, sticky=(W, E))

bmi = StringVar()
ttk.Label(mainframe, textvariable=bmi).grid(column=1, row=3, sticky=(W, E))

diagnos = StringVar()
ttk.Label(mainframe, textvariable=diagnos).grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="height").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="mass").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text=":bmi and diagnos").grid(column=3, row=3, sticky=(W, S))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=2, sticky=W)

root.bind("<Return>", calculate)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()