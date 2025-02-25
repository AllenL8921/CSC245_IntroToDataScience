#Part 1: Defining Functions (12 points)

'''
Basic Function (2 points)
Write a function add_numbers that takes two numbers and returns their sum. Implement this using both a regular function and a lambda function.

Test your function with add_numbers(3, 5) and add_lambda(3, 5).
'''

def add_numbers(num1, num2):
    return num1 + num2

# Lambda
add_lambda = lambda num1, num2 : num1 + num2

print("Basic Function \n")
print(add_numbers(3, 5))
print(add_lambda(3, 5))

'''
Flexible Function (2 points)
Modify join_words to accept an arbitrary number of words and return them concatenated into a single string with spaces. 
Implement this using both a regular function and a lambda function.

Test it with join_words("Hello", "world", "!").
'''

def join_words(*words):
    return " ".join(words)

print("Flexible Functions \n")
join_words = lambda *words : " ".join(words)
print(join_words("Hello", "world", "!"))

'''
Recursive Function (2 points)
Write a recursive function countdown(n) that prints numbers from n to 0. Test it with countdown(5).
'''
def countdown(n):
    if n < 0:
        return
    
    print(n)
    return countdown(n-1)

print("Recursive Function \n")
countdown(5)

'''
Normal Function Usage (2 points)
Write a function greet that takes a name as input and returns a greeting message. Implement this as a normal function.

Test it with greet("Alice").
'''

def greet(name):
    return "Hello " + name

print("Normal Function Usage \n")
print(greet("Alice"))

'''
Function with Default Arguments (2 points)
Write a function repeat_phrase that repeats a phrase a given number of times, with a default of 2.

Test it with repeat_phrase("Hi! ") and repeat_phrase("Hi! ", 3).
'''

def repeat_phrase(phrase, n):
    for i in range(0, n):
        print(phrase)

print("Function with Default Arguments \n")
repeat_phrase("Hi! ", 3)

'''
Higher-Order Function (2 points)
Write a function apply_function that takes a function and a value as arguments and applies the function to the value.

Test it with apply_function(lambda x: x.upper(), "hello").
'''

def apply_function(func, value):
    return func(value)

print("Higher-Order Function \n")
print(apply_function(lambda x: x.upper(), "hello"))