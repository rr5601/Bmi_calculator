def calculate_bmi(weight, height, units='metric'):
    if units == 'metric':
        # Calculate BMI using metric units (weight in kg, height in meters)
        bmi = weight / (height ** 2)
    elif units == 'imperial':
        # Calculate BMI using imperial units (weight in lbs, height in inches)
        bmi = (weight / (height ** 2)) * 703
    else:
        return "Invalid units. Please use 'metric' or 'imperial'."

    return bmi

while True:
    weight = float(input("Enter your weight (in kg or lbs): "))
    height = float(input("Enter your height (in meters or inches): "))
    units = input("Enter 'metric' for kg/m or 'imperial' for lbs/inch: ").lower()

    bmi = calculate_bmi(weight, height, units)
    print("Your BMI is:", bmi)

    choice = input("Do you want to calculate another BMI? (yes/no): ")

