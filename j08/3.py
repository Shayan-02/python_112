# lst = [1, 2, 3, 4, 5, "ali"]
# lst.pop()
# lst.pop(2)
# lst.remove("ali")
# lst.clear()
# print(lst)
# del lst

# lst = []
# for _ in range(1, 11):
#     if _ % 2 == 0:
#         lst.append(_**2)
# print(lst)

lst2 = [_**2 for _ in range(1, 11) if _ % 2 == 0]
print(lst2)