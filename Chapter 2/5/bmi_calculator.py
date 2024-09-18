height = float(input("Height (feet only): "))
height *= 12
height += float(input("Height (inches): "))
weight = float(input("Weight in pounds: "))

print(f"The BMI is {round(weight / 2.205 / (height / 39.37) ** 2, 6)}")