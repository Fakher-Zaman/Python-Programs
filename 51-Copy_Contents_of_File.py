# Copy Contents of One File to Another File using Python:

from shutil import copyfile

try:
    copyfile("D:/Python Coding/Python Programs/51-demo.txt", "D:/Python Coding/Python Programs/51-file.txt")

except Exception as e:
    print(e)

print("Copy and Paste Successfully!")