# Calculating and specifying the body max index.
# Luyanda Ntombela
# 06 March 2025


weight = eval(input("Enter your weight in kg:\n"))
height = eval(input("Enter your height in meters:\n"))
BMI = weight/height**2 
print("Your BMI is",round(BMI,2))


if BMI < 18.5 :print("Category: Underweight")
if BMI > 18.5 and BMI < 25 : print("Category: Normal weight")
if BMI  > 25 and BMI < 30 : print("Category: Overweight")
if BMI > 30 :print("Category: Obese")

