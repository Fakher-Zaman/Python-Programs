"""
Here are 14 common punctuation marks in English.

The Full Stop (.)
The Question Mark (?)
Quotation Marks/Speech Marks (” “)
The Apostrophe (‘)
The Comma (,)
The Hyphen (-)
The dash (en dash (–) em dash (—))
The Exclamation Mark (!)
The Colon (:)
The Semicolon (;)
Parentheses ()
Brackets []
Ellipsis (…)
The Slash (/), etc
"""

punctuation = '''!()-[]{};:'"\.<>./?@#$%^&*_~'''
# print(len(punctuation))

string = input("Enter anything here: ")
emptyString = ""

for i in string:
    if i not in punctuation:
        emptyString += i

print(emptyString)