for i in range(1, 41):
    if i % 3 != 0 and i % 5 == 0:
        if i == 10 or i == 20:
            continue
        if i == 35:
            break
        print(i, end=" ")
print()
j = 1
while j <= 40:
    if j % 3 != 0 and j % 5 == 0:
        if j == 10 or j == 20:
            j += 1
            continue
        if j == 35:
            break
        print(j, end=" ")
    j += 1