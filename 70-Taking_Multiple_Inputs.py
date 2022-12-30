# a, b, c = input("Enter three arguments here: ").split(",")

# print("The first argument is", a)
# print("The second argument is", b)
# print("The third argument is", c)

# print("The addition of three values =", int(a)+int(b)+int(c))

# ---> By List Comprehension:
a, b, c = [int(x) for x in input("Enter three numbers here: ").split()]
print(a)
print(b)
print(c)