def my_solution():
    file_name = input("Input the file name: ")
    file = open(f"{file_name}.txt", "r")
    for i in range(5):
        line = file.readline()
        print(line)


def teacher_solutions():
    line = ""
    counter = 0
    filename = input("Enter the name of file: ")
    infile = open(filename, "r")
    line = infile.readline()
    counter = 1
    while line != "" and counter <= 5:
        line = line.rstrip("\n")
        print(line)
        line = infile.readline()
        counter += 1
    infile.close()


teacher_solutions()
