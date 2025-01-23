# define values
num1 = int(input("enter first number: "))
op = input("enter operator(+, -, *, /): ")
num2 = int(input("enter second number: "))

# condition
if op == "+":
    print(f"sum of {num1} and {num2} is {num1 + num2}")
elif op == "-":
    print(f"difference of {num1} and {num2} is {num1 - num2}")
elif op == "*":
    print(f"product of {num1} and {num2} is {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("invalid")
    else:
        print(f"quotient of {num1} and {num2} is {num1 / num2}")
else:
    print("invalid operator")