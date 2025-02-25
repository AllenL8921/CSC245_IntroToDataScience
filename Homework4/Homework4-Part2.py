'''
Part 2: Errors and Exceptions (10 points)
Handling Errors (3 points)
Write a function safe_divide(a, b) that divides a by b, but catches the ZeroDivisionError and prints an error message instead of crashing.
'''
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

'''
Custom Exceptions (3 points)
Write a function check_age(age) that raises a ValueError with the message "Age must be a positive integer" if age is negative or not an integer.
'''

def check_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer")

'''
Handling Multiple Exceptions (2 points)
Write a function parse_int(value) that tries to convert a string to an integer and handles ValueError if the conversion fails.
'''

def parse_int(value):
    try:
        return(int(value))
    except ValueError:
        return f"{value} is not a valid integer"


'''
Finally Block (2 points)
Modify safe_divide to include a finally block that prints "Division attempted".
'''

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Zero division is not allowed"
    finally:
        print("Division completed")
