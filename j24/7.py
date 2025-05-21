num1 = int(input("enter number1: "))
op = input("enter an operator: ")
num2 = int(input("enter number2: "))
r = 0
if op == "+":
    r = num1 + num2
elif op == "-":
    r = num1 - num2
elif op == "*":
    r = num1 * num2
elif op == "/":
    if num2 != 0:
        r = num1 / num2
    else:
        print("can't devide by zero")
else:
    print("invalid operator")
print(r)
