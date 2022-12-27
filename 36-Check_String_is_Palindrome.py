# Check Whether a String is Palindrome or Not:

word = input("Enter a word here: ")
reverse = word[::-1]

if word == reverse:
    print("It is a palindrome")
else:
    print("It is not palindrome")