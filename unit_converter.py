import tkinter as tk

def cm_to_feet():
    cm = float(cm_entry.get())
    feet = cm * 0.0328084
    result_label.config(text=f"{cm} centimeters = {feet:.2f} feet")

def feet_to_inches():
    feet = float(feet_entry.get())
    inches = feet * 12
    result_label.config(text=f"{feet} feet = {inches} inches")

def sqft_to_sqm():
    sqft = float(sqft_entry.get())
    sqm = sqft / 10.764
    result_label.config(text=f"{sqft} square feet = {sqm:.2f} square meters")

def sqft_to_acres():
    sqft = float(sqft_entry2.get())
    acres = sqft / 43560
    result_label2.config(text=f"{sqft} square feet = {acres:.2f} acres")

root = tk.Tk()
root.title("Unit Conversion")

# Centimeter to Feet
cm_label = tk.Label(root, text="Centimeters:")
cm_label.grid(row=0, column=0)
cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1)
cm_button = tk.Button(root, text="Convert to Feet", command=cm_to_feet)
cm_button.grid(row=0, column=2)

# Feet to Inches
feet_label = tk.Label(root, text="Feet:")
feet_label.grid(row=1, column=0)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1)
feet_button = tk.Button(root, text="Convert to Inches", command=feet_to_inches)
feet_button.grid(row=1, column=2)

# Square Feet to Square Meters
sqft_label = tk.Label(root, text="Square Feet:")
sqft_label.grid(row=2, column=0)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=2, column=1)
sqft_button = tk.Button(root, text="Convert to Square Meters", command=sqft_to_sqm)
sqft_button.grid(row=2, column=2)

# Square Feet to Acres
sqft_label2 = tk.Label(root, text="Square Feet:")
sqft_label2.grid(row=3, column=0)
sqft_entry2 = tk.Entry(root)
sqft_entry2.grid(row=3, column=1)
sqft_button2 = tk.Button(root, text="Convert to Acres", command=sqft_to_acres)
sqft_button2.grid(row=3, column=2)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=3)
result_label2 = tk.Label(root, text="")
result_label2.grid(row=5, columnspan=3)

root.mainloop()
