""" Prompts the user for input by using the string "Tell me your password:" 
The script will then determine the ﬁrst letter of the user’s input, convert 
that letter to upper-case, and display it back. """

user_input = input("Tell me your password: ")

upper_case = user_input[0].upper()

print(f"The first letter you entered was: {upper_case}")