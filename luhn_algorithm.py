def verify_card_number(card_number):
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    card_number_reversed = translated_card_number[::-1]

    odd_digits = card_number_reversed[::2]
    sum_of_odd_digits = 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    even_digits = card_number_reversed[1::2]
    sum_of_even_digits = 0
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits

    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'


def main():
    card_number = input('Enter a credit card number: ')
    print(verify_card_number(card_number))


if __name__ == '__main__':
    main()
