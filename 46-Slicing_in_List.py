# What is Slicing on List in Python - Explained with Example:
List = ["Fakher", 578, "Zaman", [3.53, 34851], "Hammad", 582, "Shaban", 552]

# Indexing in python:
print("Through Indexing:")
print(List[0], ", ", List[-8])
print(List[1], ", ", List[-7])
print(List[2], ", ", List[-6])
print(List[3], ", ", List[-5])
print(List[4], ", ", List[-4])
print(List[5], ", ", List[-3])
print(List[6], ", ", List[-2])
print(List[7], ", ", List[-1])

# Slicing in python:
print("\nThrough Slicing:")
print(List[4:7])
print(List[0:4])
print(List[::])
print(List[::-1])
print(List[0:8:2])
print(List[-2:-6:-2])