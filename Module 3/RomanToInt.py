# Program to convert Roman numerals into decimal numbers

def convert_roman_to_decimal(roman_value):

    # Roman symbols and their decimal values
    symbols = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    # Store final result
    decimal_value = 0

    # Traverse the Roman numeral
    for index in range(0, len(roman_value) - 1):
        if symbols[roman_value[index]] < symbols[roman_value[index + 1]]:
            decimal_value -= symbols[roman_value[index]]
        else:
            decimal_value += symbols[roman_value[index]]

    return decimal_value + symbols[roman_value[-1]]

# Take Roman numeral input from user
roman_number = input("Enter a Roman numeral: ")

# Display decimal equivalent
print("Decimal equivalent:", convert_roman_to_decimal(roman_number))