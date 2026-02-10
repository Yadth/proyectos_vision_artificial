# --------------------------------------------------
# Problem 1: Sum of integers in a range
#
# Description:
# This program calculates the sum of all integers from 1 to n.
# It also calculates the sum of only the even numbers in the same range
# using a for loop.
#
# Inputs:
# - n (int): upper limit of the range
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
#
# Validations:
# - n must be an integer
# - n must be greater than or equal to 1
#
# Test cases:
# 1) Normal: n = 5 → Sum = 15, Even sum = 6
# 2) Edge case: n = 1 → Sum = 1, Even sum = 0
# 3) Error: n = -3 → Error: invalid input
# --------------------------------------------------
# input

n_text = input("Enter n: ")

try:
    n = int(n_text)

    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i

            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except ValueError:
    print("Error: invalid input")

# --------------------------------------------------
# Problem 2: Multiplication table with for
#
# Description:
# This program generates the multiplication table of a base number
# from 1 up to a given limit using a for loop.
#
# Inputs:
# - base (int): base number of the table
# - m (int): limit of the table
#
# Outputs:
# - Lines in the format: "base x i = result"
#
# Validations:
# - base must be an integer
# - m must be an integer greater than or equal to 1
#
# Test cases:
# 1) Normal: base = 5, m = 4 → prints 5x1 to 5x4
# 2) Edge case: base = 3, m = 1 → prints 3 x 1 = 3
# 3) Error: m = 0 → Error: invalid input
# --------------------------------------------------
base_text = input("Enter base number: ")
m_text = input("Enter limit: ")

try:
    base = int(base_text)
    m = int(m_text)

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            result = base * i
            print(f"{base} x {i} = {result}")

except ValueError:
    print("Error: invalid input")

# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
#
# Description:
# This program reads numbers until a sentinel value is entered.
# It calculates the average of the valid numbers.
#
# Inputs:
# - number (float)
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average>
#
# Validations:
# - Only numbers >= 0 are accepted
# - Sentinel value is -1
#
# Test cases:
# 1) Normal: 10, 20, 30, -1 → Count: 3, Average: 20
# 2) Edge case: 0, -1 → Count: 1, Average: 0
# 3) Error: -1 → Error: no data
# --------------------------------------------------

SENTINEL_VALUE = -1

total_sum = 0.0
count = 0

while True:
    number_text = input("Enter a number (-1 to finish): ")

    try:
        number = float(number_text)

        if number == SENTINEL_VALUE:
            break

        if number < 0:
            print("Error: invalid input")
            continue

        total_sum += number
        count += 1

    except ValueError:
        print("Error: invalid input")

if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print("Count:", count)
    print("Average:", average)    

# --------------------------------------------------
# Problem 4: Password attempts with while
#
# Description:
# This program allows the user to enter a password
# with a limited number of attempts.
#
# Inputs:
# - user_password (string)
#
# Outputs:
# - "Login success"
# - "Account locked"
#
# Validations:
# - Maximum attempts is limited
#
# Test cases:
# 1) Normal: correct password on second attempt → Login success
# 2) Edge case: correct password on last attempt → Login success
# 3) Error: all attempts wrong → Account locked
# --------------------------------------------------
CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break

    attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")

# --------------------------------------------------
# Problem 5: Simple menu with while
#
# Description:
# This program shows a menu that repeats until the
# user chooses to exit. It uses a while loop.
#
# Inputs:
# - option (int)
#
# Outputs:
# - Menu actions and messages
#
# Validations:
# - Option must be 0, 1, 2 or 3
#
# Test cases:
# 1) Normal: choose 1 → greeting shown
# 2) Edge case: choose 0 immediately → Bye!
# 3) Error: invalid option → error message
# --------------------------------------------------
counter = 0
option = -1

while option != 0:
    print("1) Show greeting")
    print("2) Show counter")
    print("3) Increment counter")
    print("0) Exit")

    try:
        option = int(input("Choose an option: "))
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")

    elif option == 2:
        print("Counter:", counter)

    elif option == 3:
        counter += 1
        print("Counter incremented")

    elif option == 0:
        print("Bye!")

    else:
        print("Error: invalid option")

# Problem 6: Pattern printing with nested loops

# Description:
# Prints a right-angled triangle pattern using nested for loops.

try:
    n = int(input("Enter the number of rows: "))

    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)

except:
    print("Error: invalid input")        

# Repositorio de git 
# https://github.com/Yadth/proyectos_vision_artificial    
