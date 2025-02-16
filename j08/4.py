lst = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
print(lst)
print(t)

lst[1] = "ali"
t1 = list(t)
t1[1] = "ali"
t = tuple(t1)
print(t1)