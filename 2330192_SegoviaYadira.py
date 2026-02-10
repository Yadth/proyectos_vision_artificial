# ==================================================
# Numeric and Boolean Exercises - Python
# ==================================================
# --------------------------------------------------
# Problem 1: Temperature converter and range flag
# --------------------------------------------------
# Description:
# Converts a temperature from Celsius to Fahrenheit and Kelvin.
# Also determines if the temperature is considered high.

# Inputs:
# - temp_c (float)

# Outputs:
# - Fahrenheit temperature
# - Kelvin temperature
# - High temperature flag

# Validations:
# - temp_c must be a valid float
# - temp_c must not be below absolute zero (-273.15)

# Test cases:
# 1) Normal: temp_c = 25.0
# 2) Edge: temp_c = 30.0
# 3) Error: temp_c = -300.0
temp_input = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_input)

    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15

        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 2: Work hours and overtime payment
# --------------------------------------------------
# Description:
# Calculates weekly pay considering regular and overtime hours.
# Overtime hours are paid at 150% of the normal rate.

# Inputs:
# - hours_worked (int)
# - hourly_rate (float)

# Outputs:
# - Regular pay
# - Overtime pay
# - Total pay
# - Overtime flag

# Validations:
# - hours_worked must be >= 0
# - hourly_rate must be > 0

# Test cases:
# 1) Normal: hours_worked=38, hourly_rate=100
# 2) Edge: hours_worked=40, hourly_rate=100
# 3) Error: hours_worked=-5, hourly_rate=100
hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

try:
    hours_worked = int(hours_input)
    hourly_rate = float(rate_input)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = hours_worked > 40

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 3: Discount eligibility with booleans
# --------------------------------------------------
# Description:
# Determines if a customer is eligible for a discount
# based on student status, senior status, or purchase total.

# Inputs:
# - purchase_total (float)
# - is_student_text (string)
# - is_senior_text (string)

# Outputs:
# - Discount eligibility
# - Final total after discount

# Validations:
# - purchase_total must be >= 0
# - student and senior inputs must be YES or NO

# Test cases:
# 1) Normal: total=1200, student=NO, senior=NO
# 2) Edge: total=1000, student=NO, senior=NO
# 3) Error: total=-50, student=YES, senior=NO
total_input = input("Enter purchase total: ")
student_input = input("Is student (YES/NO): ").strip().upper()
senior_input = input("Is senior (YES/NO): ").strip().upper()

try:
    purchase_total = float(total_input)

    if purchase_total < 0:
        print("Error: invalid input")
    elif student_input not in ("YES", "NO") or senior_input not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = student_input == "YES"
        is_senior = senior_input == "YES"

        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 4: Basic statistics of three integers
# --------------------------------------------------
# Description:
# Reads three integers and calculates sum, average,
# maximum, minimum, and checks if all numbers are even.

# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)

# Outputs:
# - Sum
# - Average
# - Max
# - Min
# - All even flag

# Validations:
# - Inputs must be valid integers

# Test cases:
# 1) Normal: n1=4, n2=6, n3=8
# 2) Edge: n1=0, n2=0, n3=0
# 3) Error: n1="a", n2=3, n3=5
n1_input = input("Enter first integer: ")
n2_input = input("Enter second integer: ")
n3_input = input("Enter third integer: ")

try:
    n1 = int(n1_input)
    n2 = int(n2_input)
    n3 = int(n3_input)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3

    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# --------------------------------------------------
# Description:
# Determines loan eligibility based on income,
# debt ratio, and credit score.

# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)

# Outputs:
# - Debt ratio
# - Eligibility flag

# Validations:
# - monthly_income must be > 0
# - monthly_debt must be >= 0
# - credit_score must be >= 0

# Test cases:
# 1) Normal: income=10000, debt=3000, score=700
# 2) Edge: income=8000, debt=3200, score=650
# 3) Error: income=0, debt=1000, score=600
income_input = input("Enter monthly income: ")
debt_input = input("Enter monthly debt: ")
score_input = input("Enter credit score: ")

try:
    monthly_income = float(income_input)
    monthly_debt = float(debt_input)
    credit_score = int(score_input)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# --------------------------------------------------
# Description:
# Calculates BMI and determines weight category
# using boolean flags.

# Inputs:
# - weight_kg (float)
# - height_m (float)

# Outputs:
# - BMI value (rounded)
# - Underweight flag
# - Normal flag
# - Overweight flag

# Validations:
# - weight_kg must be > 0
# - height_m must be > 0

# Test cases:
# 1) Normal: weight=60, height=1.65
# 2) Edge: weight=75, height=1.73
# 3) Error: weight=0, height=1.70
weight_input = input("Enter weight in kg: ")
height_input = input("Enter height in meters: ")

try:
    weight_kg = float(weight_input)
    height_m = float(height_input)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", bmi_rounded)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)

except ValueError:
    print("Error: invalid input")
# Repositorio de git 
# https://github.com/Yadth/proyectos_vision_artificial                           