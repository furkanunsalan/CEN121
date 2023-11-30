def main():
    file = open("names.txt", "r")
    line_counter = 0
    for line in file:
        line_counter += 1
    file.close()
    print(line_counter)


if __name__ == '__main__':
    main()
