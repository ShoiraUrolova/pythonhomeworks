def find_factors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} is a factor of {number}")
try:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        find_factors(num)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
