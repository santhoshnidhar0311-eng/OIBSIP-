def calculate_bmi(weight, height):
    # Convert height from cm to meters if needed
    if height > 3:  
        height = height / 100

    bmi = weight / (height * height)
    return bmi


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("==== BMI CALCULATOR ====\n")

    while True:
        try:
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (meters or cm): "))

            if weight <= 0 or height <= 0:
                print("Values must be positive. Try again.\n")
                continue

            bmi = calculate_bmi(weight, height)
            category = bmi_status(bmi)

            print(f"\nYour BMI : {bmi:.2f}")
            print(f"Category : {category}\n")

        except ValueError:
            print("Enter numbers only.\n")
            continue

        again = input("Calculate again? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the BMI Calculator!")
            break


if __name__ == "__main__":
    main()
