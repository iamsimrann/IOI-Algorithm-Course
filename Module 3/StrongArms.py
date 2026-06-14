# Program to check whether a number is a Narcissistic Number

# Take input from the user
num = int(input("Enter a number: "))

# Count the digits
digit_count = len(str(num))

# Initialize total
total = 0

# Process each digit
temp_num = num
while temp_num > 0:
    current_digit = temp_num % 10
    total += current_digit ** digit_count
    temp_num //= 10

# Display the result
if num == total:
    print(num, "is a Narcissistic Number")
else:
    print(num, "is not a Narcissistic Number")