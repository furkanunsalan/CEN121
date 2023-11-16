def main():
    score_1 = float(input("Enter first score: "))
    score_2 = float(input("Enter second score: "))
    score_3 = float(input("Enter third score: "))
    score_4 = float(input("Enter fourth score: "))
    score_5 = float(input("Enter fifth score: "))
    average = calc_average(score_1, score_2, score_3, score_4, score_5)
    print(f"Your grade is {determine_grade(average)} with an average score {average}")
    print("Score Number \t Score \t Grade")
    print(f"Score1: \t {score_1} \t {determine_grade(score_1)}")
    print(f"Score2: \t {score_2} \t {determine_grade(score_2)}")
    print(f"Score3: \t {score_3} \t {determine_grade(score_3)}")
    print(f"Score4: \t {score_4} \t {determine_grade(score_4)}")
    print(f"Score5: \t {score_5} \t {determine_grade(score_5)}")
    print("---------------------------------------------------")
    print(f"Average Score: \t {average} \t {determine_grade(average)}")


def calc_average(num1, num2, num3, num4, num5):
    average = (num1 + num2 + num3 + num4 + num5) / 5
    return average


def determine_grade(score):
    if 90 <= score <= 100:
        return "A"

    elif 80 <= score <= 89:
        return "B"

    elif 70 <= score <= 79:
        return "C"

    elif 60 <= score <= 69:
        return "D"

    else:
        return "F"


main()
