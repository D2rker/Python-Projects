import tkinter as tk
from tkinter import ttk, messagebox


def convert_length():
    value = float(entry_value.get())
    unit = combo_unit.get()

    if unit == "Centimeters to Meters":
        result = value / 100
        unit_result = "meters"
    elif unit == "Meters to Kilometers":
        result = value / 1000
        unit_result = "kilometers"
    elif unit == "Inches to Feet":
        result = value / 12
        unit_result = "feet"
    else:
        messagebox.showerror("Error", "Please select a valid conversion!")
        return

    label_result.config(text=f"{value} → {result:.2f} {unit_result}")


def convert_weight():
    value = float(entry_value.get())
    unit = combo_unit.get()

    if unit == "Grams to Kilograms":
        result = value / 1000
        unit_result = "kilograms"
    elif unit == "Kilograms to Pounds":
        result = value * 2.20462
        unit_result = "pounds"
    elif unit == "Pounds to Ounces":
        result = value * 16
        unit_result = "ounces"
    else:
        messagebox.showerror("Error", "Please select a valid conversion!")
        return

    label_result.config(text=f"{value} → {result:.2f} {unit_result}")


def convert_temperature():
    value = float(entry_value.get())
    unit = combo_unit.get()

    if unit == "Celsius to Fahrenheit":
        result = (value * 9 / 5) + 32
        unit_result = "°F"
    elif unit == "Fahrenheit to Celsius":
        result = (value - 32) * 5 / 9
        unit_result = "°C"
    else:
        messagebox.showerror("Error", "Please select a valid conversion!")
        return

    label_result.config(text=f"{value} → {result:.2f} {unit_result}")


def update_units(event):
    conversion_type = combo_type.get()
    units = {
        "Length": ["Centimeters to Meters", "Meters to Kilometers", "Inches to Feet"],
        "Weight": ["Grams to Kilograms", "Kilograms to Pounds", "Pounds to Ounces"],
        "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    }
    combo_unit.config(values=units[conversion_type])
    combo_unit.set("")


# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Widgets for conversion type
label_type = tk.Label(root, text="Conversion Type:")
label_type.pack(pady=5)

combo_type = ttk.Combobox(root, values=["Length", "Weight", "Temperature"])
combo_type.pack(pady=5)
combo_type.bind("<<ComboboxSelected>>", update_units)

# Widgets for unit selection
label_unit = tk.Label(root, text="Select Units:")
label_unit.pack(pady=5)

combo_unit = ttk.Combobox(root)
combo_unit.pack(pady=5)

# Widgets for input value
label_value = tk.Label(root, text="Enter Value:")
label_value.pack(pady=5)

entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=lambda: {
    "Length": convert_length,
    "Weight": convert_weight,
    "Temperature": convert_temperature
}[combo_type.get()]())
btn_convert.pack(pady=10)

# Label for result
label_result = tk.Label(root, text="Result will appear here", font=("Arial", 12))
label_result.pack(pady=10)

# Start the main loop
root.mainloop()
