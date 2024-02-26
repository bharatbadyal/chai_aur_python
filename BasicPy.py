# python output
# Python is case sensitive language
print("Welcome to Python exercises")

# can print multiple outputs with different data types
# multiple data types: string, num, float, boolean

print("Name",27,5.11,True) 

#can give seprator some value too, using which the output will be seprator by the given symbol.
# Also can assign specific end value which is by default /n newline.

print("Name",27,5.11,True,sep="-",end=";") 


# data types in Python

# integer
print(21)
# 1*10^308
print(1e308)

# decimal/Float
print(8.55)
print(1.7e308)

# Boolean
print(True,False)

# String/Text
print("This is a string")

# there will be use of type function simultaniously 
# List -> Array
print([1,2,3,4,5])
print(type(([1,2,3,4,5])))

# tuple
print((1,2,3,4,5))
print(type(((1,2,3,4,5))))

# sets
print({1,2,3,4,5})
print(type(({1,2,3,4,5})))

# Dict works on key:value principle
print({'name':"Bharat","age":27,"height":182})
print(type({'name':"Bharat","age":27,"height":182}))


# complex number
print(3+5j)


# sample function in python
def sumOfTwoNo(a,b):
  return a+b

print("sum of given two numbers is: ",sumOfTwoNo(12,5))


# Variables
# Static vs Dynamic Typing 
# Static vs Dynamic Binding
# Stylish declaration techniques
 

# the method of creating variable without giving its specific data type like in c,c++,java etc languages is called dynamic typing (python) 

# in static typing we specify the type of variable while declearing it in first hand

# dynamic binding: Means we can re initilize variable anywhere in code.
a = 5
print(a)
a="Bharat"
print(a)

# can create multiple variables at same time
a,b,c = 1,2,3

print(a,b,c)

e=f=g=14 #all with get 14 as their value
print(e,f,g)

# Keywords and Identifiers
# Keywords: in python we 32 keywords. We should not use these keywords in normal-
#  -coding rather than using these keywords for their specific use case


# Identifiers: name given to function, variable, class. This follow specfic naming convention which is majorly resemble in all the programming languages.

# identifiers can't be a keywords

# User Input
# input method by default take string as input. We can use type conversion to get value converted to desired one
# there are two type conversion : implicit and explicit
num1 = int(input('Enter Your first no: '))
num2 = int(input("Enter Your second no: "))
sum = num1 + num2 
print("Sum of given two no's:",sum)

# literals: value given to varables 

a3 = 0b1010 #binary literal
b3 = 100 #decimal literal
c3 = 0o310 #octal literal
d4 = 0x12c #hexadecimal literal

# string literals

string1 = "This is Python string"
string2 = 'This is also Python string'
char ="C"
multiline_str = """ This is multiline string
which can goes to multliline writing"""
unicode = u"\U0001f600"
raw_str =r"raw \n string"

print(string1)
print(string2)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# None : it works as placeholder
a = None
print(type(a),a)