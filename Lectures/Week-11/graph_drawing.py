import matplotlib.pyplot as plt

# Compilers are kaggle colab 

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(x_coords, y_coords)
    plt.title("Sales by Year")
    plt.xlabel("Year")
    plt.ylabel("Sales")

    plt.xticks([0, 1, 2, 3, 4], ["2016", "2017", "2018", "2019", "2020"])
    plt.yticks([0, 1, 2, 3, 4, 5], ["$0m", "$1m", "$2m", "$3m", "$4m", "$5m"])

    plt.grid(True)

    plt.show()
    plt.xlim(xmin=1, xmax=4)
    plt.ylim(ymin=1, ymax=4)

def bar_charts():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    bar_width = 5

    plt.bar(left_edges, heights, bar_width, color=("r", "g", "b", "m", "k"))
    # plt.barh() for horizontal bar charts

    plt.title("Sales by Year")
    plt.xlabel("Year")
    plt.ylabel("Sales")

    plt.xticks([5, 15, 25, 35, 45], ["2016", "2017", "2018", "2019", "2020"])
    plt.yticks([0, 100, 200, 300, 400, 500], ["$0m", "$1m", "$2m", "$3m", "$4m", "$5m"])

    plt.show()

def pie_charts():
    sales = [100, 200, 300, 400, 500]
    slice_labels = ["1st Quartes", "2nd Quarter", "3rd Quarter", "4th Quarter", "5th Quarter"]
    plt.pie(sales, labels=slice_labels, colors=('r', 'g', 'b', 'c', 'k'))
    plt.title('Sales by Quarter')
    plt.show()


pie_charts()