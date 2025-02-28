valid = ["a", "e", "i", "o", "u"]

n = input()

c = 0
for _ in n:
    if _ in valid:
        c += 1

print(2**c)
