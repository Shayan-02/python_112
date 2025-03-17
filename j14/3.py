def crona(num1, num2, num3, num4):
    n1 = num1 - num2
    n2 = num3 - num4
    if n1 > n2:
        return "Shekarestan"
    elif n2 > n1:
        return "Namakestan"
    elif n1 == n2:
        return "Equal"

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

print(crona(x1, x2, x3, x4))
