# ==================================================
# Topic: Functions in Python
# ==================================================

# --------------------------------------------------
# Problem 1: Rectangle area and perimeter
# --------------------------------------------------
# Description:
# Calculates the area and perimeter of a rectangle
# using two separate functions.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - Area
# - Perimeter
#
# Validations:
# - width > 0
# - height > 0
#
# Test cases:
# 1) Normal: width=5, height=3
# 2) Edge: width=0.1, height=0.1
# 3) Error: width=-2, height=4

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = 5
height = 3

if width > 0 and height > 0:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Grade classifier
# --------------------------------------------------
# Description:
# Classifies a numeric grade into a letter category.
#
# Inputs:
# - score (int or float)
#
# Outputs:
# - Category
#
# Validations:
# - 0 <= score <= 100
#
# Test cases:
# 1) Normal: score=85
# 2) Edge: score=100
# 3) Error: score=120

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = 85

if 0 <= score <= 100:
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: List statistics
# --------------------------------------------------
# Description:
# Returns min, max and average from a list of numbers.
#
# Inputs:
# - numbers_text (string)
#
# Outputs:
# - Min
# - Max
# - Average
#
# Validations:
# - Non-empty list
# - All values numeric
#
# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge: "5"
# 3) Error: "10,a,30"

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }

numbers_text = "10,20,30"

try:
    numbers_list = [float(n.strip()) for n in numbers_text.split(",") if n.strip() != ""]
    if len(numbers_list) == 0:
        print("Error: invalid input")
    else:
        summary = summarize_numbers(numbers_list)
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", summary["average"])
except:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 4: Apply discount list
# --------------------------------------------------
# Description:
# Applies a discount to a list of prices without
# modifying the original list.
#
# Inputs:
# - prices_list
# - discount_rate
#
# Outputs:
# - Original prices
# - Discounted prices
#
# Validations:
# - Prices > 0
# - 0 <= discount_rate <= 1
#
# Test cases:
# 1) Normal: prices=[100,200], discount=0.1
# 2) Edge: discount=0
# 3) Error: discount=1.5

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted

prices_list = [100, 200, 300]
discount_rate = 0.1

if discount_rate < 0 or discount_rate > 1 or any(p <= 0 for p in prices_list):
    print("Error: invalid input")
else:
    print("Original prices:", prices_list)
    print("Discounted prices:", apply_discount(prices_list, discount_rate))


# --------------------------------------------------
# Problem 5: Greeting function
# --------------------------------------------------
# Description:
# Creates a greeting using optional title.
#
# Inputs:
# - name
# - title (optional)
#
# Outputs:
# - Greeting message
#
# Validations:
# - name not empty
#
# Test cases:
# 1) Normal: name="Alice", title="Dr."
# 2) Edge: name="Bob", title=""
# 3) Error: name=""

def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name

    return f"Hello, {full_name}!"

name = "Alice"
title = "Dr."

if name.strip() == "":
    print("Error: invalid input")
else:
    print("Greeting:", greet(name=name, title=title))


# --------------------------------------------------
# Problem 6: Factorial function
# --------------------------------------------------
# Description:
# Calculates the factorial of a number using
# an iterative approach.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Factorial
#
# Validations:
# - n >= 0
# - n <= 20
#
# Test cases:
# 1) Normal: n=5
# 2) Edge: n=0
# 3) Error: n=-3

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5

if isinstance(n, int) and 0 <= n <= 20:
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")
# Repositorio de git:
# https://github.com/Yadth/proyectos_vision_artificial    
