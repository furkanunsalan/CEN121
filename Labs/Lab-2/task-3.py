class_a_price = 20
class_b_price = 15
class_c_price = 10


def main():
    class_a_seats = int(input("How many A Class seats were sold? "))
    class_b_seats = int(input("How many B Class seats were sold? "))
    class_c_seats = int(input("How many A Class seats were sold? "))
    print(f"Total income is ${calc_salary(class_a_seats, class_b_seats, class_c_seats)}")


def calc_salary(arg1, arg2, arg3):
    income_a = (arg1 * class_a_price)
    income_b = (arg2 * class_b_price)
    income_c = (arg3 * class_c_price)
    salary = income_c + income_b + income_a
    return salary


main()
# in lecture teacher outputted income_a, income_b, income_c
