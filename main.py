
weight = input("kg or lbs: ")

if weight == "kg":
    kg = input("Enter weight in kg: ")
    heightkg = input("Enter height in cm: ")
    bmi = int(kg) / (int(heightkg) / 100) ** 2
    print("Your BMI is: ", bmi)
elif weight == "lbs":
    lbs = input("Enter weight in lbs: ")
    heightlbs = input("Enter height in inches: ")
    bmi = (int(lbs) / (int(heightlbs) ** 2)) * 703
    print("Your BMI is: ", bmi)
else:
    print("Invalid input. Please enter kg or lbs.")