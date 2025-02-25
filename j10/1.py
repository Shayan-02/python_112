d = {"name": "ali", "age": 20, "job": "student"}
print(d.keys())
print(d.values())
print(d.items())
print()
for _ in d:
    print(d.items())

d.popitem()
print(d)