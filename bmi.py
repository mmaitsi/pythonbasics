weight=float(input("Enter the weight in kg: "))
height=float(input("Enter the height in meters: "))
bmi=weight/(height**2)
if bmi<= 19:
    print(f"{bmi}-You are under weight")
elif bmi <= 25:
    print(f"{bmi}-You are healthy")
elif bmi <= 30:
    print(f"{bmi}-You are overweight")
else:
    print(f"{bmi}-You are obese")