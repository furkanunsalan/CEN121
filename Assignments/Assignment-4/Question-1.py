import matplotlib.pyplot as plt

def solution():
    number_of_peple = [10, 45, 20, 60, 35]
    ages = ["10-20", "20-30", "30-40", "50-60", "60+"]

    plt.bar(ages, number_of_peple, color= "blue")
    plt.title("People Ages")

    plt.xlabel("Ages")
    plt.ylabel("Number of People")

    plt.show()

solution()