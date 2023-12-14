import matplotlib.pyplot as plt

def my_solution():
    spices = ["Salt", "Pepper", "Cumin", "Thyme", "Black Cumin", "Fennel", "Bay Leef", "Mint"]
    popularity = [31.4, 29.2, 12.2, 9.6, 13.8, 10.2, 17.6, 26.7]

    plt.barh(spices, popularity, color= "purple")

    plt.title("Spice Popularity In Turkey")

    plt.xlabel("Pıpularity (%)")
    plt.ylabel("Spices")

    plt.show()

my_solution()
