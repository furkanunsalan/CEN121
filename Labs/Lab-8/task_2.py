def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

position = int(input("Enter the position in the Fibonacci series you want to calculate: "))
print(f"Fibonacci number at position {position} : {fib(position)}")

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610