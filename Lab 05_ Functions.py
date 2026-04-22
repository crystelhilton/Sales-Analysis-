#Crystel Hilton
#Lab 05_ Functions

#Excercise 1  Defining & Calling Functions
def say_hello():
    print("Hello World")

say_hello()
say_hello()
say_hello()

#Exercise 2   Function with No Return
def foo(name):
    print(f'Hello {name}')

foo("Crystel")

#Exercise 3   Function with Return
def square(n):
    return n*n
print(f'The square of 2 is {square(2)}')
print(f'The square of 3 is {square(3)}')
print(f'The square of 5 is {square(5)}')

#Exercise 4   Max of Two Numbers
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

print(f"The maximum of 10 and 20 is {max_of_two(10, 20)}")
print(f"The maximum of 30 and 20 is {max_of_two(30, 20)}")
print(f"The maximum of 15 and 20 is {max_of_two(15, 20)}")

#Exercise 5   Even or Odd
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(f"Is 3 even? -> {is_even(3)}")
print(f"Is 10 even?-> {is_even(10)}")
print(f"Is 15 even?-> {is_even(15)}")

#Exercise 6   Two Parameters
def add(x, y):
    return x + y

print(f"-3 + -1 = {add(-3, -1)}")
print(f"3.5 + -1 = {add(3.5, -1)}")
print(f"3.5 + 2.5 = {add(3.5, 2.5)}")

#Exercise 7   Word Count
def count_words(sentence):
    words = sentence.split()
    return len(words)

print(f"Number of words= {count_words("My name is Crystel")}")

#Exercise 8   Initials Generator
def get_initials(*names):
    return '.'.join([name[0].upper() for name in names]) + '.'

print(f'The initials of "John Doe" are {get_initials("John", "Doe")}')
print(f'The initials of "Alice Bob Carol" are {get_initials("Alice", "Bob", "Carol")}')

#Exercise 9   Vowel Counter
def count_vowels(sentence):
    count = 0
    vowels = "aeiouAEIOU"
    
    for letter in sentence:
        if letter in vowels:
            count += 1
            
    return count

print("Vowel count:", count_vowels("Hello World"))
print("Vowel count:", count_vowels("Programming"))

#Exercise 10  Find Minimum
def find_min(numbers):
    minimum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
            
    return minimum

print(f"The minimum of [3,1,4,1,5,9,2,6,5] is {find_min([3,1,4,1,5,9,2,6,5])}")
print(f"The minimum of [-10,-20,0,10,20] is {find_min([-10,-20,0,10,20])}")

#Exercise 11  List Average 
def average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
        
    return total / count

print(f"The average of [1,2,3] is {average([1,2,3])}")
print(f"The average of [10,20,30,40,50] is {average([10,20,30,40,50])}")
print(f"The average of [5,15,25,35,45,55] is {average([5,15,25,35,45,55])}")

#Excercise 12 Square List
def square_list(numbers):
    result = []  
    
    for num in numbers:
        result = result + [num * num]  
    
    return result

print("The squares of [1,2,3,4,5] are", square_list([1,2,3,4,5]))
print("The squares of [6,-7,1.2] are", square_list([6,-7,1.2]))

#Exercise 13  Default Parameters
def greet(name, greeting="Hi"):
    print(f"{greeting} {name}")

greet("Ilia")
greet("Hao", "Hello")

#Exercise 14  Ticket price calculator 
def ticket_price(age, discount=0.1):
    base_price = 20
    
    if discount:
        return base_price - (base_price * discount)
    else:
        return base_price

print(ticket_price(25))
print(ticket_price(25, 0.2))

#Exercise 15  Voting illegibility
def can_vote(age, is_resident=True):
    if age > 18 and is_resident:
        return True
    else:
        return False

# Single parameter
print("Age: 17 can vote? ->", can_vote(17))
print("Age: 20 can vote? ->", can_vote(20))

# Two parameters
print("Age: 20 residency: False? ->", can_vote(20, False))
print("Age: 20 residency: True? ->", can_vote(20, True))
print("Age: 15 residency: True? ->", can_vote(15, True))

#Exercise 16  Greeting with Language Option
def greet(name, language="en"):
    if language == "en":
        print(f"Hello {name}")
    elif language == "es":
        print(f"Hola {name}")
    elif language == "fr":
        print(f"Bonjour {name}")

greet("Alice")
greet("Alice", "es")
greet("Alice", "fr")

#Exercise 17  Named Parameters
def calculate_cost(price, tax=0.13):
    return price + (price * tax)

print(calculate_cost(10))                 
print(calculate_cost(10, 0.2))            
print(calculate_cost(price=20, tax=0.15)) 

#Exercise 18  Global vs Local
count = 10 

def increase():
    global count
    print(f'Before increase: {count}')
    count += 1
    print(f'After increase: {count}')

increase()
print(f'Global variable after calling increase: {count}')

#Exercise 19  Using *args
def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print("multiply_all(1, 2) ->", multiply_all(1, 2))
print("multiply_all(2, 3, 4) ->", multiply_all(2, 3, 4))

#Exercise 20 Find Maximum with *args
#a
def find_max(*numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

print(find_max(3, 7, 2, 9))

print(find_max(3, 7, 2, 9))

#b
def print_shopping_list(**items):
    for item, price in items.items():
        print(f"{item}: {price}")

print_shopping_list(apple=2.5, bread=3.0, milk=4.0)

#c
def print_student_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_student_info(name="Alice", age=20, program="Computer Science")



#Execise 21 Type Annotations
def area_of_triangle(base: float, height: float) -> float:
    return base * height * 0.5

print(area_of_triangle(5, 3))
print(area_of_triangle(10, 4))

#Exercise 22 BMI calculator
def bmi(weight: float, height: float) -> float:
    return weight / (height * height)

print(bmi(70, 1.75))

#Exercise 23 Distance Formular
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f'Distance: {distance(0, 0, 3, 4)}')

#Exercise 24  Factorial Function
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f'0 factorial is {factorial(0)}')
print(f'5 factorial is {factorial(5)}')

#Exercise 25 The sum of natural numbers
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(f'The sum of first 3 natural numbers is {sum_n(3)}')
print(f'The sum of first 5 natural numbers is {sum_n(5)}')
print(f'The sum of first 10 natural numbers is {sum_n(10)}')

#Exercise 26 Power function
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f'2 raised to the power 3 is {power(2, 3)}')
print(f'5 raised to the power 4 is {power(5, 4)}')
print(f'10 raised to the power 0 is {power(10, 0)}')

#Exercise 27 String reversal
def reverse_string(s: str) -> str:
    if s == '':
        return ''
    return s[-1] + reverse_string(s[:-1])

print(f'The reverse of "hello" is "{reverse_string("hello")}"')
print(f'The reverse of "world" is "{reverse_string("world")}"')

#Exercise 28
def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(3))
print(square_lambda(3))
print(square(7))
print(square_lambda(7))

#Exercise 29
add = lambda x, y: x + y

print(add(4, 6))
print(add(-2, 10))

#Exercise 30
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("The 5th Fibonacci number is", fibonacci(5))
print("The 10th Fibonacci number is", fibonacci(10))
print("The 15th Fibonacci number is", fibonacci(15))

#Exercise 31
def sum_and_average(*nums):
    total = 0
    count = 0
    
    for num in nums:
        total += num
        count += 1
    
    return total, total / count

print(sum_and_average(1, 2, 3, 4))

#Exercise 32
def grade(score):
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

print(grade(95))
print(grade(72))

#Exercise 33
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram("listen", "silent"))

#Exercise 34
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

print("Is 3 prime? ->", is_prime(3))
print("Is 10 prime? ->", is_prime(10))
print("Is 13 prime? ->", is_prime(13))

#Exercise 35
def encrypt(text, shift=3):
    result = ""
    
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            result += chr(shifted)
        else:
            result += char
    
    return result

print("encrypt('abc', 2) ->", encrypt("abc", 2))
print("encrypt('cde', -2) ->", encrypt("cde", -2))