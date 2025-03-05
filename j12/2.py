# def fact(num: int) -> int:
#     facti = 1
#     for i in range(1, num + 1):
#         facti *= i
    
#     return facti

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))