""" Display the name of the state to the user and ask them to enter
the capital. If the user answers, incorrectly, repeatedly ask them for
the capital name until they either enter the correct answer or type the
word “exit”. """

import random

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

def guess_capital():
    while True:
        user = input(f"Enter the capital of {state}: ")
        if user.lower() == capitals_dict[state].lower():
            return "Correct"
            
        elif user.lower() == "exit":
            return f"The capital of {state} is {capitals_dict[state]} \nGoodbye!"
            


state = random.choice(list(capitals_dict))
print(guess_capital())