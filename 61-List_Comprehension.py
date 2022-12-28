friends = ["Fakher Zaman", "Hammad ASif", "Muhammad Shaban"]

# for i in friends:
#     print(i.upper())

# ---> List Comprehension Method:
# new_list = [i.upper() for i in friends]
# print(new_list)

# nums = [i for i in range(10)]
# print(nums)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in n:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

list = [i for i in range(10) if i % 2 == 0]
print(list)