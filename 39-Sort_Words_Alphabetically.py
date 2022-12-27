# Program to Sort Words in Alphabetic Order (A B C)

string = int(input("Enter the string of words here: "))

separate = string.split()
print(separate)

for i in range(len(separate)):
    separate[i] = separate[i].lower()
print(separate)

separate.sort()
print(separate)

for r in separate:
    print(r)