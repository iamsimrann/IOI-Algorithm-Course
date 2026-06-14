# Python program to print a hash (#) pattern based on the number of rows entered by the user

# Get the number of rows from user
n = int(input("Enter how many rows you want: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop for each column in the row
    for j in range(i):
        # Print hash symbol, end with space instead of new line
        print('#', end=' ')
    
    # Move to the next line after each row
    print()