n = int(input("enter a number: "))

if n % 15 == 0:
    print("feezbaaz")
elif n % 5 == 0:
    print("baaz")
elif n % 3 == 0:
    print("feez")
else:
    print(n)