amount =  float(input("enter the amount of the investment: "))
rate= float(input("enter the annual rate of return (as a percentage): "))
years= int(input("enter the number of years to calculate "))
print(f"Initial investment: ${amount:.2f}")
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate//100
        print(f"Year {year}: ${amount:.2f}")
print(invest(amount, rate, years))