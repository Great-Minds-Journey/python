
# Arithmetic Operators And Math Functions

friends = 5

#friends = friends + 1
#friends +=1
#friends = friends - 2
#friends -=2
#friends = friends * 3
#friends *=3
#friends = friends / 2
#friends /= 2
#friends = friends ** 2
#friends **= 2
#friends = friends % 2
#friends %= 2
#print(friends)


# Build in math function in python

x = 3.14
y = -4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(z, 3)
#result = max(x, y, z)
#result = min(x, y, z)

#print(result)

import math as ma

x = 9.9
print(ma.pi)
print(ma.e)
#result = ma.sqrt(x)
#result = ma.ceil(x)
#result = ma.floor(x)
#print(result)


# Exercise 1

# Cal the circumference of a circle

#radius = float(input("Enter a radius of a circle: "))

#circumference = 2 * ma.pi * radius
#print(f"The circumference is: {round(circumference, 2)}cm")

# Exercise 2

# Cal the area of a circle
#area = ma.pi * pow(radius, 2)

#print(f"The Area of the circle is: {round(area,2)}cm²")

# Exercise 3
# Cal the hypo

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = pow(a, 2) + pow(b, 2)
print(ma.sqrt(c))

