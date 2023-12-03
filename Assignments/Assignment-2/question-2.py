def main():
    file = open("names.txt", "r")
    line_counter = 0
    for line in file:
        line_counter += 1
    file.close()
    print(f"{line_counter} names are present in names.txt file")


if __name__ == '__main__':
    main()
