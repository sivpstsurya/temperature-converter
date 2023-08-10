import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

# Function to handle the conversion button click
def convert_temperature():
    if input_var.get() == '':
        output_label.config(text='Enter a temperature!')
        return

    try:
        temperature = float(input_var.get())
        if celsius_radio_var.get() == 1:
            converted_temp = celsius_to_fahrenheit(temperature)
            output_label.config(text=f'{temperature:.2f}°C = {converted_temp:.2f}°F')
        elif celsius_radio_var.get() == 2:
            converted_temp = fahrenheit_to_celsius(temperature)
            output_label.config(text=f'{temperature:.2f}°F = {converted_temp:.2f}°C')
        elif celsius_radio_var.get() == 3:
            converted_temp = celsius_to_kelvin(temperature)
            output_label.config(text=f'{temperature:.2f}°C = {converted_temp:.2f} K')
        elif celsius_radio_var.get() == 4:
            converted_temp = kelvin_to_celsius(temperature)
            output_label.config(text=f'{temperature:.2f} K = {converted_temp:.2f}°C')
        elif celsius_radio_var.get() == 5:
            converted_temp = fahrenheit_to_kelvin(temperature)
            output_label.config(text=f'{temperature:.2f}°F = {converted_temp:.2f} K')
        else:
            converted_temp = kelvin_to_fahrenheit(temperature)
            output_label.config(text=f'{temperature:.2f} K = {converted_temp:.2f}°F')
    except ValueError:
        output_label.config(text='Invalid input!')

# Create the main window
root = tk.Tk()
root.title('Temperature Converter')

# Color templates
template_bg_color = '#E5E5E5'
template_fg_color = '#333333'
template_button_bg = '#4CAF50'
template_button_fg = 'white'

# Set the background color
root.configure(bg=template_bg_color)

# Create input label
input_label = tk.Label(root, text='Enter Temperature:', bg=template_bg_color, fg=template_fg_color)
input_label.pack(pady=10)

# Create input entry
input_var = tk.StringVar()
input_entry = tk.Entry(root, textvariable=input_var)
input_entry.pack()

# Create radio buttons for temperature unit selection
celsius_radio_var = tk.IntVar()
celsius_radio = tk.Radiobutton(root, text='Celsius to Fahrenheit', variable=celsius_radio_var, value=1, bg=template_bg_color, fg=template_fg_color)
fahrenheit_radio = tk.Radiobutton(root, text='Fahrenheit to Celsius', variable=celsius_radio_var, value=2, bg=template_bg_color, fg=template_fg_color)
celsius_to_kelvin_radio = tk.Radiobutton(root, text='Celsius to Kelvin', variable=celsius_radio_var, value=3, bg=template_bg_color, fg=template_fg_color)
kelvin_to_celsius_radio = tk.Radiobutton(root, text='Kelvin to Celsius', variable=celsius_radio_var, value=4, bg=template_bg_color, fg=template_fg_color)
fahrenheit_to_kelvin_radio = tk.Radiobutton(root, text='Fahrenheit to Kelvin', variable=celsius_radio_var, value=5, bg=template_bg_color, fg=template_fg_color)
kelvin_to_fahrenheit_radio = tk.Radiobutton(root, text='Kelvin to Fahrenheit', variable=celsius_radio_var, value=6, bg=template_bg_color, fg=template_fg_color)

celsius_radio.pack()
fahrenheit_radio.pack()
celsius_to_kelvin_radio.pack()
kelvin_to_celsius_radio.pack()
fahrenheit_to_kelvin_radio.pack()
kelvin_to_fahrenheit_radio.pack()

# Create the conversion button
convert_button = tk.Button(root, text='Convert', command=convert_temperature, bg=template_button_bg, fg=template_button_fg)
convert_button.pack(pady=10)

# Create the output label
output_label = tk.Label(root, text='', bg=template_bg_color, fg=template_fg_color)
output_label.pack()

# Start the main loop
root.mainloop()
