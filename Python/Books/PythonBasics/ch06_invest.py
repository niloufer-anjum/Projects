""" Tracks the growing amount of an investment over time. """
def invest(amount, rate, years):
    for i in range(1, years+1):
        amount = amount + (amount * rate)
        print(f"Year {i}: ${amount:.2f}")


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of return: "))
years = int(input("Enter years to invest: "))
invest(principal, rate, years)