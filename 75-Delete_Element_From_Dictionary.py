# Solution # 1 (Using del statement)
marks = {"fakhar":90, "hammad":90, "shaban":85, "ali":80}
print(marks)
del marks["ali"]
print(marks)

# Solution # 2 (Using pop() function)
marks = {"fakhar":90, "hammad":90, "shaban":85, "ali":80}
print(marks)
marks.pop("ali")
marks.pop("shaban")
print(marks)