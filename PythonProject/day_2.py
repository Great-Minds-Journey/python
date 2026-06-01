# TypeCasting = the process of converting a variable from one type to another
#                     str(), int(), float(), bool()
from day_1 import quantity

name = "numbu collins"
age = 24
gpa = 3.12
is_student = True

print(type(name))
print(type(age))
print(type(is_student))


gpa = int(gpa)



# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

#names = input("what is your name?: ")
#ages = input("How old are?: ")
#print(f"Hey you are welcome {names}")
#print(f"You are {ages} years old")


# Exercise 1 Rectangle Area Calc

#length = float(input("Enter the length: "))
#width = float(input("Enter the Width: "))
#area = length * width

#print(f"The area is: {area}cm²")

# Exercise 2 shopping Cart Programme
item = input("What item would you like to buy?: ")
price = float(input("What is the price? "))
quantity = int(input("What quantity would you like?: "))

total = price * quantity
print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: {total}cfa")