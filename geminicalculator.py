from tkinter import *

# Function to update the expression in the entry field
def button_click(char):
    global expression
    expression += str(char)
    input_field.set(expression)

# Function to clear the entry field
def button_clear():
    global expression
    expression = ""
    input_field.set("")

# Function to evaluate the expression and display the result
def button_equal():
    try:
        global expression
        result = str(eval(expression))
        input_field.set(result)
        expression = result
    except:
        input_field.set("Error")

def button_equal():
        try:
            global expression
            result = str(eval(expression))
            input_field.set(result)
            expression = result  # Update expression for subsequent calculations
        except:
            input_field.set("Error")

# Main function
if __name__ == "__main__":
    # Create the main window
    window = Tk()
    window.title("Simple Calculator")
    window.geometry("1000x500")


    # Global variable to store the expression
    expression = ""

    # Entry field to display the expression
    input_field = StringVar()
    entry = Entry(window, textvariable=input_field, width=50, borderwidth=15)
    entry.grid(columnspan=5, padx=20, pady=20)

    # Buttons for numbers and operators
    button_7 = Button(window, text="7", command=lambda: button_click(7), width=5, height=2)
    button_7.grid(row=1, column=0)
    button_8 = Button(window, text="8", command=lambda: button_click(8), width=5, height=2)
    button_8.grid(row=1, column=1)
    button_9 = Button(window, text="9", command=lambda: button_click(9), width=5, height=2)
    button_9.grid(row=1, column=2)
    button_div = Button(window, text="/", command=lambda: button_click("/"), width=5, height=2)
    button_div.grid(row=1, column=3)

    button_4 = Button(window, text="4", command=lambda: button_click(4), width=5, height=2)
    button_4.grid(row=2, column=0)
    button_5 = Button(window, text="5", command=lambda: button_click(5), width=5, height=2)
    button_5.grid(row=2, column=1)
    button_6 = Button(window, text="6", command=lambda: button_click(6), width=5, height=2)
    button_6.grid(row=2, column=2)
    button_mul = Button(window, text="*", command=lambda: button_click("*"), width=5, height=2)
    button_mul.grid(row=2, column=3)

    button_1 = Button(window, text="1", command=lambda: button_click(1), width=5, height=2)
    button_1.grid(row=3, column=0)
    button_2 = Button(window, text="2", command=lambda: button_click(2), width=5, height=2)
    button_2.grid(row=3, column=1)
    button_3 = Button(window, text="3", command=lambda: button_click(3), width=5, height=2)
    button_3.grid(row=3, column=2)
    button_sub = Button(window, text="-", command=lambda: button_click("-"), width=5, height=2)
    button_sub.grid(row=3, column=3)

    button_0 = Button(window, text="0", command=lambda: button_click(0), width=5, height=2)
    button_0.grid(row=4, column=0)
    button_dot = Button(window, text=".", command=lambda: button_click("."), width=5, height=2)
    button_dot.grid(row=4, column=1)
    button_clear = Button(window, text="C", command=button_clear, width=5, height=2)
    button_clear.grid(row=4, column=2)
    button_add = Button(window, text="+", command=lambda: button_click("+"), width=5, height=2)
    button_add.grid(row=4, column=3)  # Added the missing closing parenthesis here
    button_equal = Button(window, text="=", command=button_equal, width=5, height=2)
    button_equal.grid(row=5, column=0, columnspan=4)
    

    window.mainloop() 