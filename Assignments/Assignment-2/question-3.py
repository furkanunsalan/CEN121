def main():
    line = ""
    line_index = 1
    file_name = input("What is the name of the file? ")
    file = open(file_name, "r")
    for line in file:
        content = line.rstrip("\n")
        print(f"{line_index}: {content}")
        line_index += 1
    file.close()


if __name__ == '__main__':
    main()
