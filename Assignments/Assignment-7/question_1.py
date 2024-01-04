def multiply(x, y):
    if y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

result = multiply(5, 3)
print(f"Multiplication of given numbers is {result}")
