#Crystel Hilton Lab 10

'''Classes and Objects
Professor Class
Create a class that models a college professor
Class Name:Professor Constructor: (__ init __)
The constructor should:
• Accept two parameters:
▪ name the professor's name
▪ department the department that belong to
• Store both values in instance variables'''
#Instance Method: greet
#Takes no additional arguments.
#Returns a string introducing the professor in the format:
#Hello, my name is <name> and I teach in <department>.
#Hint: Use f-string for this'''

#Question 1
class Professor:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        
    def greet(self):
        return f"Hello, my name is {self.name} and I teach in {self.department}."
    
#Question2 
'''Test harness'''
ilia = Professor('Ilia', 'ICET')
print(ilia.greet())

sonali = Professor('Sonali', 'Math')
print(sonali.greet())
    

'''Instructor Class
Create a class that represents a college instructor.
This is similar to the previous class that you built but with the following changes: constructor takes
an additional argument, the greet method is replaced by the __ str __ and two additional
methods are added
Class Name:Instructor
Constructor (__ init __)'''
#The constructor should: Accept three parameters:
#name - the instructor's name
#department - the department they belong to
#courses - a list of the courses taught by this instructor (optional: default value should
#be None)
#Store name and department in instance variables
#for the courses parameter:

#Question 3  
class Instructor:
    def __init__(self, name, department, courses=None): #the object data
        self.name = name
        self.department = department

        # handle None case  If it is None store an empty list Otherwise, store the provided list
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
    def __str__(self):
              return f"Hello, my name is {self.name} and I teach {self.courses} in {self.department}."

    def add_course(self, course):
        self.courses.append(course) 

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)


            #Test harness
print(f'\nCreating first object')
ilia = Instructor('Ilia', 'ICET', 'Python, Data Science'.split(', '))
print(ilia)
course = 'Machine Learning'
print(f'Adding course: {course}')
ilia.add_course(course)
print(ilia)
print(f'\nCreating second object')
arben = Instructor('Arben', 'ICET', ['Java', 'Databases'])
print(arben)
course = 'Java'
print(f'Removing course: {course}')
arben.remove_course(course)
print(arben)

#Question 4 
'''ShippingCart Class
Create a class that represents a grocery shopping cart.
The class should include a class attribute: a dictionary that stores the prices of each items.'''

class ShippingCart:
    prices = {'apple': 2.5, 'banana': 1.3, 'orange': 1.8}

    def __init__(self, name):  #__init__ constructor
        self.name = name   #owner of the cart
        self.items = [] #what is inside the cart

    def __str__(self):
        return f"{self.name}'s cart: {self.items}, total price: ${self.calculate_cart_price():.2f}"

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def remove_item(self, item):
        self.items = [i for i in self.items if i[0] != item]

    def calculate_cart_price(self):
        total = 0
        for item, quantity in self.items:
            price = ShippingCart.prices.get(item, 1) #using get() as key is not in dictionary
            total += price * quantity
        return total


# Test harness
cart = ShippingCart('Narendra')
print(f'{cart}\n')
item, qty = 'apple', 3
print(f'Adding {qty} {item} to cart')
cart.add_item(item, qty)
item, qty = 'banana', 5
print(f'Adding {qty} {item} to cart')
cart.add_item(item, qty)
item, qty = 'pear', 2
print(f'Adding {qty} {item} to cart')
cart.add_item(item, qty)
print(f'{cart}\n')
item = 'apple'
print(f'Removing {item} from the cart')
cart.remove_item('apple')
print(f'{cart}\n')
