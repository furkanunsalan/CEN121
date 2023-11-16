mass = float(input("Input the mass of your object in kilograms: "))
weight = mass * 9.8

if weight > 500:
    print(f"Your object is too heavy. It's {weight:,.2f} newtons")

elif weight < 100:
    print(f"Your object is too light. It's {weight:,.2f} newtons")

else:
    print(f"Your objects weight is normal. It's {weight:,.2f} newtons")
