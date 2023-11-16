width1 = int(input("Width of the first rectangle: "))
height1 = int(input("Height of the first rectangle: "))
width2 = int(input("Width of the second rectangle: "))
height2 = int(input("Width of the first rectangle: "))

area1 = width1 * height1
area2 = width2 * height2

print(f"Area 1: {area1}, Area 2: {area2}")

if area1 > area2:
    print(f"Area of the first rectangle is greater than the second one by {area1-area2} units.")

elif area2 > area1:
    print(f"Area of the second rectangle is greater than the first one by {area2-area1} units.")

else:
    print("Areas are equal")
