height = float(input("Height in m: "))
weight = float(input("Weight in kg: "))
print()

bmi = weight / height ** 2
print(f"Your BMI is {round(bmi, 5)}")

category = ""
if bmi < 15:
    category = "very severely underweight"
elif bmi <= 16:
    category = "severely underweight"
elif bmi <= 18.4:
    category = "underweight"
elif bmi <= 24.9:
    category = "normal weight"
elif bmi <= 29.9:
    category = "overweight"
elif bmi <= 34.9:
    category = "moderately obese"
elif bmi <= 39.9:
    category = "severely obese"
else:
    category = "morbidly obese"

print("BMI Category:", category)