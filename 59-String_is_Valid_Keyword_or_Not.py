# How to Check if a String is a Valid Keyword or Not?

import keyword

words = ["break", "string", "name", "python", "for", "end", "while", "lambda", "continue", "text", "list", "try"]

for i in range(len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i], "is a keyword in python.")
    else:
        print(words[i], "is not keyword in python.")

print("\n\n", keyword.kwlist)