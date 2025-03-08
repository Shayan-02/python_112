def validator(pID):
    sum_chars = 0
    for _ in range(10, 1, -1):
        sum_chars += (_ * int(pID[10 - _]))
    result = sum_chars % 11
    return "yes" if int(pID[-1]) == (result if result == 0 or result == 1 else 11 - result) else "no"
    if result == 0 or result == 1:
        return "yes" if int(pID[-1]) == result else "no"
    else:
        return "yes" if int(pID[-1]) == 11 - result else "no"

n = input()
print(validator(n))
