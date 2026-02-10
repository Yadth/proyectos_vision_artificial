# --------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# --------------------------------------------------
# Description:
# Creates and manages a shopping list using list operations.
# Allows adding items, counting elements, and searching products.

# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)

# Outputs:
# - Items list
# - Total items
# - Found item (True/False)

# Validations:
# - initial_items_text not empty
# - new_item and search_item not empty

# Test cases:
# 1) Normal: "apple:2,banana:5", new_item="milk", search="apple"
# 2) Edge: single item
# 3) Error: empty input
initial_items_text = input("Enter initial items: ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    items_raw = initial_items_text.split(",")

    items_list = []

    for item in items_raw:
        product = item.split(":")[0].strip().lower()
        items_list.append(product)

    new_item = input("Enter new item: ").strip().lower()
    search_item = input("Enter item to search: ").strip().lower()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        items_list.append(new_item)

        is_in_list = search_item in items_list

        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", is_in_list)
# --------------------------------------------------
# Problem 2: Points and distances with tuples
# --------------------------------------------------
# Description:
# Creates two points in a 2D plane using tuples.
# Calculates the distance between them and the midpoint.

# Inputs:
# - x1, y1, x2, y2 (float)

# Outputs:
# - Point A
# - Point B
# - Distance
# - Midpoint

# Validations:
# - Inputs must be valid floats

# Test cases:
# 1) Normal: (0,0) and (3,4)
# 2) Edge: same points
# 3) Error: invalid number input
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# --------------------------------------------------
# Description:
# Manages a small product catalog using a dictionary.
# Calculates the total price based on product and quantity.

# Inputs:
# - product_name (string)
# - quantity (int)

# Outputs:
# - Unit price
# - Quantity
# - Total price
# OR error message if product is not found

# Validations:
# - product_name must not be empty
# - quantity must be greater than 0
# - product must exist in dictionary

# Test cases:
# 1) Normal: apple, 3
# 2) Edge: banana, 1
# 3) Error: product not found
product_prices = {
    "apple": 10.0,
    "banana": 8.5,
    "orange": 12.0
}

product_name = input("Enter product name: ").strip().lower()

try:
    quantity = int(input("Enter quantity: "))

    if product_name == "" or quantity <= 0:
        print("Error: invalid input")

    elif product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)

    else:
        print("Error: product not found")

except ValueError:
    print("Error: invalid input")
# --------------------------------------------------
# Problem 4: Student grades with dict and list
# --------------------------------------------------
# Description:
# This program manages student grades using a dictionary where
# each student name is associated with a list of grades. It calculates
# the average grade and determines if the student passed.
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - "Grades:" <grades_list>
# - "Average:" <average>
# - "Passed:" True|False
#
# Validations:
# - student_name must not be empty after strip()
# - student_name must exist in the dictionary
# - grades list must not be empty
#
# Test cases:
# 1) Normal: student_name = "alice"
# 2) Edge case: student_name = "bob"
# 3) Error: student_name = "david"

grades_dict = {
    "alice": [90.0, 85.0, 88.0],
    "bob": [70.0, 65.0, 72.0],
    "carol": [95.0, 100.0, 92.0]
}

student_name = input("Enter student name: ").strip().lower()

if student_name == "":
    print("Error: invalid input")
elif student_name not in grades_dict:
    print("Error: student not found")
else:
    grades_list = grades_dict[student_name]

    if len(grades_list) == 0:
        print("Error: no grades available")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0

        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", is_passed)
# --------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# --------------------------------------------------
# Description:
# This program counts the frequency of each word in a sentence.
# It converts the sentence to lowercase, removes basic punctuation,
# stores the words in a list, and uses a dictionary to count how
# many times each word appears.

# Inputs:
# - sentence (string)

# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>

# Validations:
# - sentence must not be empty after strip()
# - words list must not be empty

# Test cases:
# 1) Normal: "Hello world hello"
# 2) Edge case: "hi hi bye bye"
# 3) Error: "     "

# --------------------------------------------------

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: invalid input")
else:
    # normalize sentence
    sentence = sentence.lower()

    # remove basic punctuation
    for char in ".,!?;:":
        sentence = sentence.replace(char, "")

    # convert to list of words
    words_list = sentence.split()

    if not words_list:
        print("Error: empty words list")
    else:
        # build frequency dictionary
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # find most common word
        most_common_word = ""
        max_count = 0

        for word, count in freq_dict.items():
            if count > max_count:
                max_count = count
                most_common_word = word

        # outputs
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)
# --------------------------------------------------
# Problem 6: Simple address book (dictionary CRUD)
# --------------------------------------------------
# Description:
# This program manages a simple address book using a dictionary.
# It allows the user to add, search, or delete contacts.
# Each contact has a name and a phone number.
#
# Inputs:
# - action_text (string): "ADD", "SEARCH", or "DELETE"
# - name (string): contact name
# - phone (string): phone number (only for ADD)
#
# Outputs:
# - "Contact saved:" name phone
# - "Phone:" phone
# - "Contact deleted:" name
# - "Error: contact not found"
# - "Error: invalid action"
#
# Validations:
# - action_text must be ADD, SEARCH, or DELETE
# - name must not be empty after strip()
# - phone must not be empty for ADD
#
# Test cases:
# 1) Normal: ADD, "Alice", "1234567890"
# 2) Edge case: SEARCH "Alice"
# 3) Error: DELETE "Unknown"
# --------------------------------------------------

# Initial contacts dictionary
contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210",
    "Carlos": "5556667777"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Enter contact name: ").strip().title()

    if name == "":
        print("Error: invalid name")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()
            if phone == "":
                print("Error: invalid phone")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")                
# Repositorio de git 
# https://github.com/Yadth/proyectos_vision_artificial                   
