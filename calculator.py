import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a string variable to hold the input and output
input_text = tk.StringVar()

# Create an Entry widget to display the input/output
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 30), bd=10, insertwidth=6, width=18, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Function to update the input field
def button_click(number):
    current = input_text.get()
    input_text.set(current + str(number))

# Function to clear the input field
def button_clear():
    input_text.set("")

# Function to evaluate the input expression
def button_equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Error")

# Create the calculator buttons without subtraction and division
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 8), ('+', 4, 3),
]
# Add the buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18,), command=button_equal ).grid(row=5, column=1, rowspan=2)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Add the clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=button_clear).grid(row=4, column=2)
tk.Button(root, text='Del', padx=20, pady=20, font=('Arial', 18), command=button_click).grid(row=5, column=0)
# Run the application
root.mainloop()
