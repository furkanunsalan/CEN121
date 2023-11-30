
def file_writing():
    file_object = open("data.txt", "w")
    file_object.write('John Locke \n')
    file_object.write('David Hume \n')
    file_object.write('Edmund Burke \n')
    file_object.close()


def file_reading():
    file = open("data.txt", "r")
    file_contents = file.read()
    file.close()
    print(file_contents)


def line_reading():
    file = open("data.txt", "r")
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    file.close()
    print(line1)
    print(line2)
    print(line3)


def writing_input_to_file():
    print("Enter the name of your friends")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("Friend #3: ")

    data = open("data.txt", "w")
    data.write(name1 + '\n')
    data.write(name2 + '\n')
    data.write(name3 + '\n')
    data.close()
    print("Name are written to file")


def writing_numbers():
    file = open("numbers.txt", "w")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))
    file.write(str(num1) + '\n')
    file.write(str(num2) + '\n')
    file.write(str(num3) + '\n')
    file.close()


def test():
    file = open("data.txt", "r")
    line3 = file.readlines()[2]
    print(line3)


writing_numbers()
