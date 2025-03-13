import tkinter as tk
from tkinter import messagebox


from calculator import add, subtract, multiply, divide


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.resizable(False, False)
window.configure(bg="#f0f0f0")


frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(expand=True, fill="both", padx=10, pady=10)


expression = ""


result_var = tk.StringVar()
result_var.set("0")


def press(num):
    global expression
    expression = expression + str(num)
    result_var.set(expression)


def equal_press():
    try:
        global expression
        
       
        if not expression:
            return
        
      
        if '+' in expression:
            num1, num2 = map(float, expression.split('+'))
            result = add(num1, num2)
        elif '-' in expression:
            # Handle possible negative numbers by finding the last '-'
            last_minus = expression.rfind('-', 1)
            if last_minus != -1:
                num1 = float(expression[:last_minus])
                num2 = float(expression[last_minus+1:])
                result = subtract(num1, num2)
            else:
                num1, num2 = map(float, expression.split('-'))
                result = subtract(num1, num2)
        elif '*' in expression:
            num1, num2 = map(float, expression.split('*'))
            result = multiply(num1, num2)
        elif '/' in expression:
            num1, num2 = map(float, expression.split('/'))
            result = divide(num1, num2)
        else:
            result = expression
            
       
        result_var.set(result)
        expression = str(result)
        
    except Exception as e:
        result_var.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    result_var.set("0")


display = tk.Entry(frame, textvariable=result_var, font=("Arial", 20), bd=10, relief=tk.FLAT, 
                  justify="right", bg="white")
display.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

button_params = {
    'font': ('Arial', 14),
    'bd': 5,
    'relief': tk.RAISED,
    'padx': 15,
    'pady': 10,
    'bg': '#e0e0e0'
}


button1 = tk.Button(frame, text="1", command=lambda: press(1), **button_params)
button2 = tk.Button(frame, text="2", command=lambda: press(2), **button_params)
button3 = tk.Button(frame, text="3", command=lambda: press(3), **button_params)
button4 = tk.Button(frame, text="4", command=lambda: press(4), **button_params)
button5 = tk.Button(frame, text="5", command=lambda: press(5), **button_params)
button6 = tk.Button(frame, text="6", command=lambda: press(6), **button_params)
button7 = tk.Button(frame, text="7", command=lambda: press(7), **button_params)
button8 = tk.Button(frame, text="8", command=lambda: press(8), **button_params)
button9 = tk.Button(frame, text="9", command=lambda: press(9), **button_params)
button0 = tk.Button(frame, text="0", command=lambda: press(0), **button_params)


button_plus = tk.Button(frame, text="+", command=lambda: press('+'), **button_params, bg='#ff9e0d')
button_minus = tk.Button(frame, text="-", command=lambda: press('-'), **button_params, bg='#ff9e0d')
button_multiply = tk.Button(frame, text="*", command=lambda: press('*'), **button_params, bg='#ff9e0d')
button_divide = tk.Button(frame, text="/", command=lambda: press('/'), **button_params, bg='#ff9e0d')
button_equal = tk.Button(frame, text="=", command=equal_press, **button_params, bg='#4caf50')
button_clear = tk.Button(frame, text="C", command=clear, **button_params, bg='#f44336')
button_dot = tk.Button(frame, text=".", command=lambda: press('.'), **button_params)


button7.grid(row=1, column=0, sticky="nsew")
button8.grid(row=1, column=1, sticky="nsew")
button9.grid(row=1, column=2, sticky="nsew")
button_divide.grid(row=1, column=3, sticky="nsew")

button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")
button_multiply.grid(row=2, column=3, sticky="nsew")

button1.grid(row=3, column=0, sticky="nsew")
button2.grid(row=3, column=1, sticky="nsew")
button3.grid(row=3, column=2, sticky="nsew")
button_minus.grid(row=3, column=3, sticky="nsew")

button0.grid(row=4, column=0, sticky="nsew")
button_dot.grid(row=4, column=1, sticky="nsew")
button_clear.grid(row=4, column=2, sticky="nsew")
button_plus.grid(row=4, column=3, sticky="nsew")

button_equal.grid(row=5, column=0, columnspan=4, sticky="nsew")


for i in range(6):
    frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    window.mainloop() 
