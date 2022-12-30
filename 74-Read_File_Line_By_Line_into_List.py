# ---> Solution # 1 (Using readlines())

# file = open("74-file.txt", "r")
# lines = file.readlines()
# # print(lines)
# new_lines = [x.strip() for x in lines]
# print(new_lines)

# ---> Solution # 2 (For Loop and List Comprehension)

file = open("74-file.txt", "r")
lines = [lines for lines in file]
# print(line)
new_lines = [x.strip() for x in lines]
print(new_lines)