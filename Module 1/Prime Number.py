# Python program to determine whether a number is a prime number

# Take input from the user
number = int(input("Enter an integer: "))

# Check if the number is greater than 1
if number > 1:
    # Test divisibility up to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        # If divisible, it is not a prime number
        if number % divisor == 0:
            print(f"{number} is a composite number.")
            break
    else:
        # No divisors found, so it is prime
        print(f"{number} is a prime number.")
else:
    # Numbers less than or equal to 1 are not prime
    print(f"{number} is neither prime nor composite.")