from random import randint


def main():
    counter = 0
    file = open("random_numbers.txt", "w")
    counter_limit = int(input("How many times do you want to write random numbers to file? "))
    while counter <= (counter_limit - 1):
        random_number = randint(1, 500)
        file.write(f"{random_number}\n")
        counter += 1
    file.close()
    print(f"{counter_limit} random numbers are generated and written to the file.")


if __name__ == '__main__':
    main()
