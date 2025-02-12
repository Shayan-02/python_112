lst = [1, "ali", "reza", 5, 7, True, None]

lst.append("mohsen")

print(lst)
print(lst[2])
lst.insert(2, "mohammad")
print(lst)
lst[3] = "mohammad" + " " + "reza"

lst.pop()
lst.pop(3)
lst.remove("ali")
del lst[2]
lst.clear()