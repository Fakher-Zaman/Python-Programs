# Accessing Index of List using for Loop in Python:

# Solution # 1(Using Enumerate Method:)
List = [10, 20, 30, 40, 50]
for index, value in enumerate(List):
    print(index, value)

# Solution # 1(Using For Loop Method:)
List = [10, 20, 30, 40, 50]
for index in range(len(List)):
    value = List[index]
    print(index, value)