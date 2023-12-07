from random import randint


def my_solution():
    numbers = []
    for i in range(7):
        random_number = randint(0, 9)
        numbers.append(random_number)
        if i <= 6:
            print(numbers[i], end="")


def teacher_solution():
    number_list = [0] * 7
    for i in range(7):
        number_list[i] = randint(0, 9)
    for i in range(7):
        print(number_list[i], end="")


my_solution()
