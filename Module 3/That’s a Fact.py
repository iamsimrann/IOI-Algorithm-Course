# Program to find all divisors of a given number

# Checks every value from 1 to the number and prints those that divide evenly
def display_divisors(num):
    print("The divisors of", num, "are:")
    
    for value in range(1, num + 1):
        if num % value == 0:
            print(value)

# Taking input from the user
user_num = int(input("Enter a number to find its divisors: "))

# Calling the function
display_divisors(user_num)