import random


def main():
    current_number = 0
    odd_counter = 0
    even_counter = 0
    total_numbers = 100

    for counter in range(total_numbers):
        current_number = random.randint(1, 100)
        if is_even(current_number):
            even_counter += 1

        else:
            odd_counter += 1

    print(f"Out of {total_numbers} numbers, there were {even_counter} even numbers and {odd_counter} odd numbers.")


def is_even(number):
    if number % 2 == 0:
        return True

    else:
        return False


main()
