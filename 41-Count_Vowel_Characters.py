# Program to Count the Number of Each Vowel:

# Solution # 1(By using dictionary)
# string = input("Enter the string: ")
# vowels = "aeiou"

# string = string.casefold()
# count = {}.fromkeys(vowels, 0)    # dictionary

# for char in string:
#     if char in count:
#         count[char] += 1

# print(count)

# Solution # 2(By using List and dictionary comprehension)
string = input("Enter the string: ")
vowels = "aeiou"

string = string.casefold()
count = {key:sum([1 for char in string if char == key]) for key in vowels}

print(count)
