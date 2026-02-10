# ==================================================
# String Exercises - Python
# ==================================================
# --------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# --------------------------------------------------
# Description:
# This program receives a full name as a single string,
# normalizes it (removes extra spaces and fixes case),
# and displays the name in Title Case along with its initials.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - Formatted name in Title Case
# - Initials in the format X.X.X.
#
# Validation:
# - The input must not be empty after strip()
# - The name must contain at least two words
#
# Test cases:
# 1) Normal: "juan carlos tovar"
# 2) Edge case: "  MARIA   LOPEZ  "
# 3) Error: "   "

def format_full_name(full_name):
    full_name = full_name.strip()

    if full_name == "":
        print("Error: invalid input")
        return

    words = full_name.split()

    if len(words) < 2:
        print("Error: full name must contain at least two words")
        return

    formatted_name = full_name.title()
    initials = ""

    for word in words:
        initials += word[0].upper() + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")
# ---------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# --------------------------------------------------
# Description:
# Validates a basic email structure by checking:
# - Exactly one '@'
# - At least one '.' after '@'
# - No spaces allowed
# If valid, displays the email domain.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - Valid email: True / False
# - Domain (if valid)
#
# Validation:
# - Email must not be empty
# - No spaces allowed
#
# Test cases:
# 1) Normal: "user@example.com"
# 2) Edge case: "test@mail.co"
# 3) Error: "invalid email@"

def validate_email(email_text):
    email_text = email_text.strip()

    if email_text == "":
        print("Error: invalid input")
        return

    if " " in email_text:
        print("Valid email: False")
        return

    if email_text.count("@") != 1:
        print("Valid email: False")
        return

    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]

    if "." not in domain_part:
        print("Valid email: False")
        return

    print("Valid email: True")
    print(f"Domain: {domain_part}")    
# --------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# --------------------------------------------------
# Description:
# Checks whether a phrase is a palindrome,
# ignoring spaces and letter case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - Is palindrome: true / false
#
# Validation:
# - Phrase must not be empty
# - Minimum length after cleaning: 3 characters
#
# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Edge case: "oso"
# 3) Error: "  "

def check_palindrome(phrase):
    phrase = phrase.strip()

    if phrase == "":
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("Error: phrase too short")
        return

    reversed_phrase = normalized_phrase[::-1]

    is_palindrome = normalized_phrase == reversed_phrase
    print(f"Is palindrome: {is_palindrome}")
# --------------------------------------------------
# Problem 4: Sentence word statistics
# --------------------------------------------------
# Description:
# Analyzes a sentence and displays word statistics:
# count, first word, last word, shortest and longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word
#
# Validation:
# - Sentence must not be empty
#
# Test cases:
# 1) Normal: "Python is very powerful"
# 2) Edge case: "Hello"
# 3) Error: "   "

def sentence_statistics(sentence):
    sentence = sentence.strip()

    if sentence == "":
        print("Error: invalid input")
        return

    words = sentence.split()

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")
# --------------------------------------------------
# Problem 5: Password strength classifier
# --------------------------------------------------
# Description:
# Classifies a password as weak, medium, or strong
# based on length and character variety.
#
# Rules:
# - Weak: length < 8
# - Medium: length >= 8 but missing some strong criteria
# - Strong: length >= 8 and contains uppercase, lowercase,
#           digit, and symbol
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - Password strength: weak / medium / strong
#
# Validation:
# - Password must not be empty
#
# Test cases:
# 1) Normal: "Abc123!@"
# 2) Edge case: "password1"
# 3) Error: ""

def password_strength(password_input):
    if password_input == "":
        print("Error: invalid input")
        return

    length = len(password_input)

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if length < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")
# --------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# --------------------------------------------------
# Description:
# Creates a product label with a fixed length of 30 characters.
# If the label is shorter, it is padded with spaces.
# If it is longer, it is truncated.

# Inputs:
# - product_name (string)
# - price_value (string or number)

# Outputs:
# - Label with exactly 30 characters

# Validation:
# - Product name must not be empty after strip()
# - Price must be a positive number

# Test cases:
# 1) Normal: product_name="Apple", price=10
# 2) Edge: product_name="A", price=1
# 3) Error: product_name="   ", price=-5       
# # Repositorio de git 
# https://github.com/Yadth/proyectos_vision_artificial            
