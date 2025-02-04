start = int(input("start number: "))
end = int(input("end number: "))
i = end

while i >= start:
    if i % 3 == 0 and i % 7 != 0:
        print(i, end=" ")
    i -= 2