def validate_isbn(isbn, length):
    # Check if ISBN length matches expected length
    if len(isbn) != length:
        if length == 10:
            print("ISBN-10 code should be 10 digits long.")
        else:
            print("ISBN-13 code should be 13 digits long.")
        return

    given_check_digit = isbn[length - 1]

    # Validate characters
    for index, char in enumerate(isbn):
        if not char.isdigit():
            if length == 10 and char == "X" and index == length - 1:
                continue
            else:
                print("Invalid character was found.")
                return

    # Extract main digits (exclude check digit)
    main_digits = isbn[0:length - 1]
    main_digits_list = [int(digit) for digit in main_digits]

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare check digits
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    # Check format
    if ',' not in user_input:
        print("Enter comma-separated values.")
        return

    values = user_input.split(',')

    if len(values) != 2:
        print("Enter comma-separated values.")
        return

    isbn = values[0]

    try:
        length = int(values[1])
    except ValueError:
        print("Length must be a number.")
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# Run the program
main()