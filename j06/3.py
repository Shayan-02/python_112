a = "hello world"

for i in a:
    if i == "l":
        a = a.replace("l", "*")
    print(i, end=" ")
print()
print(a)