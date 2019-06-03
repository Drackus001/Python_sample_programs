#Numbers: int, float, complex
#Operations: + - * /

x = 28 #int
y = 28.4587 #float 

#int < float < complex
print(int(y)) #type convertion float into int number

print(complex(y)) #type convertion float into complex number

#Arithmetic Operation

a = 2
b = 6.0 
c = 12 +0j

#Rule: Widen numbers so they're same type

#addition
print(a + b) #result in float = 8.0
print(a + a) #result in int = 4

#subtraction
print(b - a)
print(a - b) #result in negative 2 - 6.0  = -4.0

#multiplication
print(a * b) #result in float = 12.0

#division
print(b / a) #result in float = 3.0
print(c / b) #result in complex = (2 + 0j)

#modulo (remainder in division) eg:5%2 = 1
print(b % a) #result = 0.0

#quotient 16//5 = 3
print(10//3) #result = 3 



