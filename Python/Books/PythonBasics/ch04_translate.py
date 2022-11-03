""" Asks the user for some input with the following prompt: Enter some text:
Then use the .replace() method to convert the text entered by the user into 
“leetspeak” by making changes to lower-case letters."""

text = input("Enter some text: ")

leet_speak = text.replace('a', '4').replace('b', '8').replace('e', '3').replace('l', '1').replace('o', '0').replace('s', '5').replace('t', '7')

print(leet_speak)