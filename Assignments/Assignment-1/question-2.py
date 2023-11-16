print(f"Radius\tSphere Volume")
print("----------------------")


for r in range(1, 7):
    pi = 3
    volume = (4/3) * pi * r**3
    print(f"{r}\t{volume}")
