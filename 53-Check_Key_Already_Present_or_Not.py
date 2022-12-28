# Program to Check if a Key is Already Present in a Dictionary

dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
key = int(input("Enter a key here: "))

if key in dict.keys():
    print("It is already present!")
else:
    print("It is not present!")