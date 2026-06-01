# IF STATEMENT

# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter you age: "))
if age > 100:
    print("you are too old to sign up")
elif age >=18:
    print("You are now signed up!")
elif age < 0:
    print("The age you inputted is not valid  ")

else:
    print("You must be 18+ to sign up!")


    # Next example (checking if a user actually enters his/her name)

#name = input("What is your name?: ")

#if name == "":
    #print("You did not type in your name!")
#else:
    print(f"You are welcome {name}")


    # Exercise (python calculator)
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
  result =num1 + num2
  print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"The operator {operator} is not valid")