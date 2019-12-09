# Ex 1
var = input("What is your name?\n")
print("Hello, " + var + "!")

# Ex 2
import math
print("Please type two numbers\n")
number_one = float(input("Number one: "))
number_two = float(input("Number two: "))
division = math.ceil(number_one / number_two)
print("The rounded up division is: {}".format(division))

# Ex 3
radius = float(input("Please type a radius: \n"))
print("The area is {:.2f} m2".format(math.pi * radius ** 2))

# Extra ex
print("Pocket Calculator \n" )
calc = input(">> ")
print(eval(calc))