baseSugar = 1.5
baseButter = 1
baseFlour = 2.75


def cookie():
    cookie_request = float(input("How many cookies do you want to make? "))
    needed_sugar = (cookie_request * baseSugar) / 48
    needed_butter = (cookie_request * baseButter) / 48
    needed_flour = (cookie_request * baseFlour) / 48
    print(f"You need {needed_sugar} cups of sugar, {needed_butter} cups of butter, {needed_flour} cups of flour.")


cookie()
