# Program to perform basic mathematical operations

# Function to calculate addition
def addition(a, b):
    return a + b

# Function to calculate subtraction
def subtraction(a, b):
    return a - b

# Function to calculate multiplication
def multiplication(a, b):
    return a * b

# Function to calculate division
def division(a, b):
    return a / b

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

print("Addition Result:", addition(first_num, second_num))
print("Subtraction Result:", subtraction(first_num, second_num))
print("Multiplication Result:", multiplication(first_num, second_num))
print("Division Result:", division(first_num, second_num))