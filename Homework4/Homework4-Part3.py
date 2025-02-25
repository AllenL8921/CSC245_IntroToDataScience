import itertools
'''
Part 3: Iterators (12 points)
Using Built-in Iterators (4 points)
Use the built-in iter and next functions to iterate over a list of numbers [5, 4, 3, 2, 1] manually.
'''

print("Iterators \n")
numList = [5,4,3,2,1]
iterator = iter(numList)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

'''
Using Generator Expressions (4 points)
Use a generator expression to create an iterator that yields uppercase versions of words in a list. Iterate over it using a for loop.
'''

print("Using Generator Expressions \n")
words = ["hello", "world", "data", "is", "awesome"]
uppercase_words = (word.upper() for word in words)

for word in uppercase_words:
    print(word)

'''
Custom Iterator Class (2 points)
Write a custom iterator class Countdown that counts down from a given number to zero.
'''

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current +1

countdown = Countdown(5)

print("Custom Iterator Class \n")
for number in countdown:
    print(number)

'''
Using itertools (2 points)
Use the itertools.cycle function to cycle through a list of colors ["red", "blue", "green"] indefinitely and print the first 6 values.
'''
color_list = ["red", "blue", "green"]

color_cyle = itertools.cycle(color_list)

print("Using itertools \n")
for i in range(0, 6):
    print(next(color_cyle))