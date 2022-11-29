from tkinter import *


def calculate():
    miles = int(input.get())
    km = miles * 1.609344
    equal_label["text"]=round(km, 2)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=1, row=0)
input.get()

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

equal_label = Label(text="0")
equal_label.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()