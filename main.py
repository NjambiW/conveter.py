from tkinter import *


def conversion():
    miles = float(user_input.get())
    km = miles * 1.609
    kilometers_number.config(text=str(km))


window = Tk()
window.title("miles to Km Converter")
window.minsize(width=250, height=150)
# creates a entry to enter the number to be converted
user_input = Entry(width=7)
user_input.grid(column=5, row=4)

miles_label = Label(text="miles", font=("courier", 12, "normal"))
miles_label.grid(column=6, row=4)
miles_label.config(pady=5, padx=5)

kilometers_label = Label(text="is equal to", font=("courier", 12, "normal"))
kilometers_label.grid(column=5, row=5)
kilometers_number = Label(text=f"0", font=("courier", 12, "normal"))
kilometers_number.grid(column=6, row=5)
kilometers_unit = Label(text="Km", font=("courier", 12, "normal"))
kilometers_unit.grid(column=9, row=5)


# creates the calculation button
calculation = Button(text="Calculate", command=conversion)
calculation.grid(column=5, row=6)
calculation.config(pady=20, padx=5)

window.mainloop()
