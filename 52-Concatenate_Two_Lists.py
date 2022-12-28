# Solution no. 1 (By using + operator):
l1 = [1, 2, 3, 4, "a", "b", "c"]
l2 = [1, 2, 3, 4, "d", "e", "f"]
l12 = l1 + l2
print(l12)


# Solution no. 2 (By using unique elements)
l12 = list(set(l1 + l2))
print(l12)

# Solution no. 3 (By using extend() function)
l1.extend(l2)
print(l1)