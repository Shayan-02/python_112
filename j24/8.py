from tkinter import messagebox

num1 = int(input("enter number1: "))
op = input("enter an operator: ")
num2 = int(input("enter number2: "))

if op == "+" or op == "-" or op == "*" or op == "/":
    r = 0
    if op == "+":
        r = num1 + num2
    elif op == "-":
        r = num1 - num2
    elif op == "*":
        r = num1 * num2
    elif op == "/":
        try:
            r = num1 / num2
        except Exception as e:
            print(e)
        finally:
            print("finally")
    print(r)
else:
    messagebox.showerror("invalid operator", "operator is invalid")
