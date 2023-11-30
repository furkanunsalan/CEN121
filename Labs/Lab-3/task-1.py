def main():
    numbers = open("numbers.txt", "r")
    contents = numbers.read()
    numbers.close()
    print(contents)


if __name__ == '__main__':
    main()
