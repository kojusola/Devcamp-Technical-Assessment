# function to check if a string is a palindrome
def is_palindrome():
    # enters raw string
    string=input("Enter string: ")
    # check if a string is the same as when the string is reversed usimg indexing.
    # if the same return yes else return no
    if string==string[::-1]:
        print("Yes")
    else:
        print("No")
is_palindrome()