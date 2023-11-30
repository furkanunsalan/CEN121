def my_solution():
    file = open("numbers.txt", "r")
    counter = 0
    total = 0.0
    while counter <= 2:
        line = file.readline()
        total = total + float(line)
        counter += 1
    file.close()
    print(f"Total is {total}")


def teacher_solution():
    line = ""
    total = 0.0
    number = 0.0

    infile = open("numbers.txt", "r")
    for line in infile:
        number = float(line)
        total += number
    infile.close()
    print("Total: ", total)


my_solution()
