roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
loopStop = False

while not loopStop:
    number = int(input("Enter a number between 1-10: "))
    roman_index = number - 1

    if 1 <= number <= 10:
        print(f"Number\tRomen Numeral")
        print("----------------------")
        print(f"{number}\t{roman_numerals[roman_index]}")
        loopStop = True

    else:
        print("ERROR! Please select a number between 1-10")
        pass
