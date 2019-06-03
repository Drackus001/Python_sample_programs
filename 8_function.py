def ping():
    return "Ping!..."
import math

#print(dir())

def volume(r):
    """Returns the volume of a spere with radius r. """ #doc string
    v = (4.0/3.0) * math.pi * r**3
    return v

volume(2)

#print(help(volume)) #returns the documentation of string (doc string of function)

#Keyword Arguments
def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters. """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

#valid pcalling function
print(cm(feet=5)) 

print(cm(inches=70))

print(cm(feet=5 ,inches = 8))

print(cm(inches = 8, feet = 5))

#typoes of arguments: keyword arguments(default arguments), required arguments
#required arguments should be from left-to-right  


