# Find Numbers Divisible by Another Number

# Solution # 1 (By using for loop and conditional statement):
print("The numbers are divisible by 13 from (1-100):")
# for i in range(1, 100):
#     if i % 13 == 0:
#         print(i)
    
# Solution # 2: (By using lambda() and filter() function)
result = list(filter(lambda x : x % 13 == 0, range(1, 100)))
print(result)