day = 1
bug = 0

for x in range(5):
    if day < 5:
        bug += int(input(f"How many bugs did you collect on day {day}? "))
        day += 1
    elif day == 5:
        bug += int(input(f"How many bugs did you collect on day {day}? "))

print(f"Total of {bug} bugs collected in {day} days!")
