def my_solution():

    number_list = [6, 15, 55, 4, 28, 9, 32]
    number_to_compare = 7

    def compare_numbers(a, b):
        index = 0
        for item in a:
            if a[index] <= b:
                index += 1
            else:
                print(a[index])
                index += 1

    compare_numbers(number_list, number_to_compare)


def teachers_solutions():
    def display_numbers_greater_than_n(numbers, n):
        for i in numbers:
            if i > n:
                print(i)

    numb_list = [6, 15, 55, 4, 28, 9, 32]
    comparing = 7
    display_numbers_greater_than_n(numb_list, comparing)


my_solution()
