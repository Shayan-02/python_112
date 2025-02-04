n1 = int(input("enter a number: "))
n2 = str(n1)[::-1]

print("yes" if n1 == int(n2) else "no")