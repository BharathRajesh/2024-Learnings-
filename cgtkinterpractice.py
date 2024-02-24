import tkinter as tk

def on_button_click():
    input_text = entry.get()
    label_result.config(text=f"You entered: {input_text}")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("1200x500")

# Create a label
label = tk.Label(root, text="Enter something:")

# Create an entry widget (input box)
entry = tk.Entry(root)

# Create a button
button = tk.Button(root, text="Click me!", command=on_button_click)

# Create a label to display the result
label_result = tk.Label(root, text="")

# Pack the widgets into the window
label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
