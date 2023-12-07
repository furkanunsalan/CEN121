def solution():
    weekly_sales = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        sales = float(input(f"Enter sales for {day}: "))
        weekly_sales.append(sales)
    total_sales = sum(weekly_sales)
    print(f"\n Total sales for the week: {total_sales:.2f}")


solution()
