# How to Check if a List is Empty in Python

# Solution # 1(Using Boolean Operation):
# print(bool([10, 20, 30]))
my_list = list(input("Enter a list: "))
# if not my_list:
#     print("The list is empty!")
# else:
#     print("The list = ", my_list)

# Solution # 2(Using len() Operation):
# if len(my_list) == 0:
#     print("The list is empty!")
# else:
#     print("The list = ", my_list)

# Solution # 3(Using Square Brackets):
if my_list == []:
    print("The list is empty!")
else:
    print("The list = ", my_list)