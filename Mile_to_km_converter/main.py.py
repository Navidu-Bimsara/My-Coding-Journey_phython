from tkinter import *

def miles_to_km():
    # 1. Get the string from the entry box
    miles = float(miles_input.get())
    # 2. Do the math (1 mile = 1.609 km)
    km = round(miles * 1.609)
    # 3. Update the label with the result
    km_result_label.config(text=f"{km}")

# Setup the Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20) # Adds space around the edges

# Row 0: Input and "Miles" Label
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Row 1: "is equal to", Result, and "Km"
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Row 2: The Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()