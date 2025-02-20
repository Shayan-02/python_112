s1 = {"apple", "banana", "cherry"}
s2 = {"microsoft", "apple", "asus"}

s7 = s1.difference(s2)
s8 = s1.intersection(s2)
s9 = s1.symmetric_difference(s2)

s1.difference_update(s2)
# s1.symmetric_difference_update(s2)
s1 = s1.symmetric_difference(s2)
s1.add("apple")
del s1