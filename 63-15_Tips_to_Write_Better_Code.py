# 15 Tips and Tricks to Write a Better Python Code

print("---> Tip # 1 (Multiple Checks in if statement):")
marks = 80
# Simple Way
if marks == 90 or marks == 80 or marks == 95:  
    print("Good Job!")
# Efficient Way
if 80 in [90, 80, 95]:  
    print("Good Job!")

print("\n---> Tip # 2 (ShortHand if-else statement):")
# Simple Way
if marks > 90:
    print("Excellent Work!")
else:
    print("Good Job!")
# Efficient Way
print("Excellent Work!") if marks > 90 else print("Good Job!")

print("\n---> Tip # 3 (List Comprehension):")
l = [50, 60, 70, 80, 90]
# Simple Way
a = []
for i in l:
    a.append(i * 2)
print(a)
# Efficient Way
x = [i * 2 for i in l]
print(x)

print("\n---> Tip # 4 (Using Enumerate Function):")
l = [10, 20, 30, 40, 50]
# Simple Way
index = 0
for i in l:
    print(index, i)
    index += 1
# Efficient Way
for i in enumerate(l):
    print(i)

print("\n---> Tip # 5 (Using _ as separators):")
# Simple Way 
num1 = 9000000
num2 = 10000
add = (num1 + num2)
print(add)
# Efficient Way
num1 = 90_00_000
num2 = 10_000
add = (num1 + num2)
print(f'{add:,}')

print("\n---> Tip # 6 (lambda() function):")
# Simple Way
def square(x):
    return x*x
print(square(4))
# Efficient Way
a = lambda b: b**2
print(a(4))

print("\n---> Tip # 7 (Zip Function):")
# Simple Way
print("Joe has scored 90 marks in math")
print("Harry has scored 60 marks in art")
print("Peter has scored 80 marks in biology")
print("Smith has scored 95 marks in computer", "\n")
# Effiecient Way
names = ["Joe", "Harry", "Peter", "Smith"]
marks = [90, 60, 80, 95]
subjects = ["math", "art", "biology", "computer"]
for name, mark, subject in zip(names, marks, subjects):
    print(name, "has scored", mark, "marks in", subject)

print("\n---> Tip # 8 (Protect Password in Terminal):")
# Normal Way
# username = input("Enter username: ")
# password = input("Enter password: ")
print("Login Successfully!")
# Efficient Way
from getpass import getpass
# username = input("Enter username: ")
# password = getpass("Enter password: ")
# print(password)

print("\n---> Tip # 9 (Using sets to sort the unique values):")
# Normal Way
my_list = [10, 30, 20, 40, 30, 40, 60, 40, 50, 30, 20]
print(my_list)
# Efficient Way
my_set = set(my_list)
print(list(my_set))

print("\n---> Tip # 10 (Format string with f string):")
# Normal Way
name = "fakher zaman"
print("My name is", name)
num1 = 16
num2 = 34
print("The addition of", num1, "and", num2, "is", num1+num2)
# Efficient Way
print(f'\nMy name is {name}')
print(f'The addition of {num1} and {num2} is {num1+num2}')

print("\n---> Tip # 11 (Using sorted to sort the complex iterables):")
l = [40, 20, 10, 30, 60, 50]
sorted_list = sorted(l)
# sorted_list = sorted(l, reverse=True)
print(sorted_list)
dl = [{"name": "fakher zaman", "marks": 85},
      {"name": "hammad asif", "marks": 85},
      {"name": "muhammad shaban", "marks": 80},
      {"name": "ali raza", "marks": 80}]
sorted_data = (sorted(dl, key=lambda x:x["marks"]))
print(sorted_data)

print("\n---> Tip # 12 (Merge dictionaries using **):")
dict1 = {"Name": "fakher zaman", "Marks": "90%"}
dict2 = {"Level": "BS", "Degree": "IT"}
mergeDict = {**dict1, **dict2}
print(mergeDict)

print("\n---> Tip # 13 (Unpacking using _ and * variable)")
# a, b, *c = (10, 20, 30, 40, 50)
a, b, *c, d = (10, 20, 30, 40, 50, 60, 70)
print(a)
print(b)
print(c)
print(d)

print("\n---> Tip # 14 (Generators to save the memory)")
# Normal Way
import sys
ls = [i for i in range(90000)]
print(sum(ls))
print(sys.getsizeof(ls), "bytes")
# Efficient Way
generator = (j for j in range(90000))
print(sum(generator))
print(sys.getsizeof(generator), "bytes")

print("\n---> Tip # 15 (Using .join to Concatenate Strings)")
ls = ["welcome", "to", "Python"]
# Normal Way
a = ""
for i in ls:
    a += i + " "
print(a)
# Efficient Way
a = " ".join(ls)
print(a)