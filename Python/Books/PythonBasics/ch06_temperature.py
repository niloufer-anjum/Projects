""" Prompts the user to enter a temperature in de-
grees Fahrenheit and then display the temperature converted to Cel-
sius. Then prompts the user to enter a temperature in degrees Celsius and
display the temperature converted to Fahrenheit. All converted temperatures are to 2 decimal places """

def convert_cel_to_far(temp):
    far = temp * 9/5 + 32
    print(f"{temp} degrees Celcius is {far:.2f} degrees Fahreheit")

def convert_far_to_cel(temp):
    cel = (temp - 32) * 5/9
    print(f"{temp} degrees Fahrenheit is {cel:.2f} degrees Celcius")


celcius = float(input("Enter the temperature in Celcius: "))
convert_cel_to_far(celcius)

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
convert_far_to_cel(fahrenheit)
