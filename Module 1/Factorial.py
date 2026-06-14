# Calculate the product sequence of a number using recursion
def recursive_product(num):
    if num == 1:
        return num
    else:
        return num * recursive_product(num - 1)

value = int(input("Enter a value: "))

# Check for invalid input
if value < 0:
    print("This operation cannot be performed on negative values.")
elif value == 0:
    print("The result for 0 is 1")
else:
    print("The result for", value, "is", recursive_product(value))