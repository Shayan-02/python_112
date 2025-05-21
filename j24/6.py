def calculate_sum(n):
    numbers = [i for i in range(1, n + 1)]
    sum_result = sum(numbers)
    summation_string = " + ".join(map(str, numbers)) + " = " + str(sum_result)
    return summation_string
n = int(input())
print(calculate_sum(n))
