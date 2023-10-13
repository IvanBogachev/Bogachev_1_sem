from tkinter import *
from tkinter import ttk

f calculate(*args):
    try:
    bmi.set(eval(primer))
    except ValueError:
        pass


root = Tk()

root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

primer = StringVar()
primer_entry = ttk.Entry(mainframe, width=7, textvariable=primer)
primer_entry.grid(column=1, row=1, sticky=(W, E))

otvet = StringVar()
ttk.Label(mainframe, textvariable=bmi).grid(column=1, row=3, sticky=(W, E))

ttk.Label(mainframe, text="height").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="mass").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text=":bmi and diagnos").grid(column=3, row=3, sticky=(W, S))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=2, sticky=W)

root.bind("<Return>", calculate)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()