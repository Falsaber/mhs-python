#Simple math equations can easily be solved using Python. You have access to a good amount of symbols to use for this purpose (+,-,*,/,%).

#Addition
add = 2 + 2
print(add)

#Subtraction
subtract = 95 - 65
print(subtract)

#Multiplication
times = 5 * 6
print(times)

#Division
divide = 88 / 2
print(divide)

#Exponentials
power = 9 ** 3
print(power)

#Modulo (Remainder)
remain = 3 % 2
print(remain)

#Once variables are defined, they can also be used to perform more complex equations, like calculating the tip for a meal:
meal = 21.50
tax = 0.05
tip = 0.2
#Note that variables can actually be redefined by their previous definitions! This allows us to set a new value for "meal" and after, "total":
meal = meal + meal * tax
total = meal + meal * tip
#And then, we can find the total, using the modulo function.
print("%.2f" % total)
