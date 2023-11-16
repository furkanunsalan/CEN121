n = 5

for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)

for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)
