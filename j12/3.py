def fibonacci(n, cache={1: 1, 2: 1}):
    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b


print(fibonacci(500))