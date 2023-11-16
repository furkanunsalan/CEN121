import time

print("I will identify if a number is even or odd between 1-100")

for num in range(1, 101):
    if num % 2 != 0:
        oddText = f"{num} is an odd number"
        print(oddText)
        time.sleep(0.2)
    else:
        evenText = f"{num} is an even number"
        print(evenText)
        time.sleep(0.2)
