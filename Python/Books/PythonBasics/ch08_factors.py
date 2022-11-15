""" Asks the user to input a positive integer and then prints out the factors of that number. """
def factors(number):
    for i in range(1, number+1):
        if number%i == 0:
            print(f"{i} is a factor of {number}")

number = int(input("Enter a positive integer: "))
factors(number)