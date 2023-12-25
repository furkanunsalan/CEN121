def solution():
    year = 1903
    file = open("Assignments/Assignment-5/WorldSeriesWinners.txt", "r")
    winning_times = {}
    winner_by_year = {}

    while True:
        input_year = int(input("Enter a year between 1903-2006: "))

        if input_year >= 1903 and input_year <= 2006:
            for line in file:
                line = line.strip()

                if line in winning_times:
                    winning_times[line] += 1
                else:
                    winning_times[line] = 1

                winner_by_year[year] = line
                year += 1

            file.close()
            print(f"The {input_year} winner is {winner_by_year[input_year]}. They won total of {winning_times[winner_by_year[input_year]]} time(s).")
            break
        else:
            print("Invalid year.")

solution()
# For the given values in WorldSeriesWinners.txt, 
# years 2007 and 2008 are invalid so I excluded them from the program.
