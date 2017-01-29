# Exercise 5: More Variables and Printing
# Refrence:https://github.com/wzpan/Learn-Python-The-Hard-Way/blob/master/Python3/ex05.py
my_name = 'xilu'
my_age = 25 # DO NOT ASK GIRL'S AGE PLEASE
my_height = 160 # cm
my_weight = 50 # kg
my_eyes = 'black'
my_teeth = 'White'
my_hair = 'black'

print ("Let's talk about %s." % my_name)
print ("She's %d cm tall." % my_height)
print ("She's %d kg heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("Her teeth are usually %s depending on the coffee." % my_teeth)

print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
