#Crystel Hilton Lab 03

#Exercise 1 (Boolean Expressions & Comparison Operators 1-3)
age= int(input('Enter your age'))
print(f"age > 18 {age > 18}") 

#Exercise 2
num1= float(input('Enter the first number'))
num2= float(input('Enter the second number'))
print(f'num1 < num2 {num1 < num2}')

#Exercise 3
x = 10
print(f"x == 10 {x==10}")
print(f"x != 5 {x !=5}")
print(f"x >= 7 {x >=7}")

#Exercise 4  (Simple If Statement 4-7)
user_input= int(input("Enter a number"))
if user_input > 0:
       print(f'{user_input} is a positive number')

#Exercise 5 
pay= float(input ("Enter your hourly payrate"))
if pay <7.50:
       print(f'Error:{pay} is below the minimum $7.50')

#Exercise 6
user= str(input("Enter a string"))
if user != (''):
       print(f'You entered {user}')

#Exercise 7
Test_score= float(input("Enter a test score(for example 97 or 98)"))
if Test_score >=90:
       print(f'your score of {Test_score} is exellent')

#Exercise 7 (duplicate number) (If-Else Statement 7-10)
int_eger= int(input('Enter and integer'))
if int_eger % 2 == 0:
   print("Even")
else:
      print("Odd")

#Exercise 8
user_name= input("Enter a user name")
if user_name == '':
      print("You must Enter a username")
else:
      print(f"Welcome {user_name}")

#Exercise 9a
password= input("Enter a password")
if password == "20Python123":
      print("Access granted")
else:
      print("Access Denied")

#Exercise 9b
payrate= float(input("enter your hourly pay rate "))
hours= float(input("Enter your hours worked"))
grosspay= payrate*hours
if grosspay <=300:
      witholding_tax= grosspay*0.10
else:
      withholding_tax= grosspay* 0.12
netpay= grosspay- witholding_tax
print(f'Gross pay:${grosspay},Witholding Tax:{witholding_tax}%,Net Pay:${netpay}')

#Exercise 10  '3 runs are needed to determine if it works correctly'
Bank_Savings= float(input("Enter the number of years your money was left in the bank"))
if Bank_Savings > 5:
      interest= 7.5
else:
      interest= 5.4
print(f'Your interest rate is: {interest}')

#Exercise 11 (Nested If/ If-Elif-Else)

grade= (input("Enter your grade (e.g A, B, C, D, F)"))
if grade == "A":
      print("Excellent")
elif grade == "B":
      print("Good")
elif grade == "C":
      print("Average")
elif grade == "D":
      print("Poor")
elif grade == "F":
      print("Fail")
else:
      print("Grade Not Valid")

#Exercise 12  'otherwise'
pension= int(input("Enter your age"))
Service= int(input("Enter your years of service"))
if pension >= 65:
      print("Eligible for pension")
else:
      if Service > 10:
            print("Eligible for pension")
      else:
            print("Not eligible")

#Exercise 12 Duplicate (similar to 7)
int1= int(input('Enter a number'))
if int1>0: #checks if the number is positive
      if int1 % 2 == 0: #determines whether it is even or odd
            print("Even Number")
      else: #conditions
            print("Odd Number")
else:
            print("Negative Number")

#Exercise 13
number1= int(input("Enter first number"))
number2= int(input("Enter second number"))
letter= (input("Enter a letter(In Caps"))
if letter=="A":
      print (number1+number2)
elif letter=="S":
      print (number1-number2)
elif letter=="M":
      print (number1*number2)
else:
      print(number1/number2)

#Exercise 14 Logical Operators (and, or)
leap_year= int(input("Enter a year"))
if (leap_year % 4 ==0) and (leap_year % 100 !=0) or (leap_year % 400 ==0):
      print("Leap Year")
else:
      print("Not a Leap Year")

#Exercise 15
numA= input("Enter the first number")
numB= input("Enter the second number")
if numA > 0 and num2 > 0:
      print("Both positive")
elif numA > 0 or numB > 0:
      print("At least one positive")
else:
      print("No Positives")

#Simple Matching
colours= input("Enter a color: red, green or blue")
match colours:
      case "red":
            print("You chose red!")
      case "green":
            print("you chose green!")
      case "blue":
            print("You chose blue!")
      case _:
            print("unknown color")
#Matching multiple values
day= input("Enter a day of the week").lower()
match day:
      case "saturday"| "sunday":
            print ("Weekend")
      case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
            print("Weekday")
      case _:
            print ("Invalid")

#Variable Binding
x= int(input("Enter x coordinate"))
y= int(input("Enter y coordinate"))
point= (x, y)
match point:
      case (0,0):
            print("Origin")
      case (x,0):
            print(f'On the X-axis {x}')
      case (0,y):
            print(f'On the Y-axis {y}')
      case (x,y):
            print(f'Point at x={x}, y={y}')

#Guards (with if)
intA= int(input("Enter an integer"))
match intA:
      case x if x <0:
            print("The number is negative")
      case x if x % 2==0:
            print("The number is even")
      case _:
            print("The number is odd")
#Combining Patterns
num_ber= int("Enter a number betweem 1 and 10")
match num_ber:
      case 1:
            print("One")
      case 2|3:
            print("Two or Three")
      case x if x >5:
            print("Greater than 5")
      case _: #otherwise
            print("Other Number")

#Matching Sequences
names= [["Alice", "Bob"], ["Alice", "Bob", "Charlie"], ["Alice", "Bob", "Charlie","David"]]
for name in names:
      match names:
            case [x,y]:
                  print(f'Two names: {x}, {y}')
            case [x,y,z]:
                  print(f'Three names:{x}, {y}, {z}')
            case [x, *y, z, ]: #*middle elelments in list join-prints middle names
                  print(f'Many names: {x},{"".join(y)} {z}')
#Matching Dictionaries
student= {"name": "Sara", "id": 123, "program": "Computer Science"}
match student:
      case {"name":name, "id": id}:
            print(f"Name {name}, ID: {id}")
      case {"name": name,"Program": program}:
            print(f'Name {name}, Program {program}')
      case _:
            print("Unkown Student Data")
#Matching Classes
pointx= int(input("Enter X coordinate"))
pointy= int(input("Enter Y coordinate"))
point= (x, y)
match point:
      case (0,0):
           print("Origin")
      case (x,0):
           print(f" On x-axis at x={x}")
      case (0,y):
           print(f" on y-axis at y={y}")
      case (x,y):
            print(f"Point at x={x}, y={y}")

