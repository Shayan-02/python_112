n = int(input("Enter a number: "))


n1 = n // 10
n2 = n % 10

print(n1 is n2)

if n1 == n2:
    print("yes")
else:
    print("no")

print(type(n2) is int)