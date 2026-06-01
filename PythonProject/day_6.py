# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"
#print("positive" if num > 0 else "negative")
#result = "EVEN" if a % 2== 0 else "ODD"
#print(result)
#max_num = a if a > b else b
#print(max_num)
#min_num = b if b < a else a
#print(min_num)
#status = "Adult" if age >=18 else "Child"
#print(status)
#weather = "HOT" if temperature > 20 else "COLD"
#print(weather)
#access_level = "Full Access" if user_role =="admin" else "Limited Access"
#print(access_level)


# STRINGS Method

#phone_number = input("Enter a phone number: ")
#name = input("Enter your full name: ")
#result = len(name)
#result = name.find("s")
#result = name.rfind("m")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#name= name.isdigit()
#result = name.isalpha()
#phone_number = phone_number.count("-")
#phone_number= phone_number.replace("-", " ")
#print(help(str))



# Validate user input  Exercise
# 1. username is no more than 12 characters
# 2, username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")
if len(username) > 12 :
     print("Your username can't be more than 12 characters!")
elif not username.find(" ")== -1:
    print("Your username can't contain spaces ")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
     print(f"Welcome: {username}")
