def main():
    rainfall_amount = []

    for month in ["January", "February", "March", "April",
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"]:
        rainfall_input = int(input(f"Enter a number for rainfall amount in {month}: "))
        rainfall_amount.append(rainfall_input)

    total_rainfall = sum(rainfall_amount)
    average_rainfall = total_rainfall / 12
    min_rainfall = min(rainfall_amount)
    max_rainfall = max(rainfall_amount)

    print("Name \t Value")
    print("-------------")
    print(f"Total Rainfall \t {total_rainfall}")
    print(f"Average Rainfall \t {average_rainfall}")
    print(f"Minimum Rainfall \t {min_rainfall}")
    print(f"Maximum Rainfall \t {max_rainfall}")


if __name__ == '__main__':
    main()
