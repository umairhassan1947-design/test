# this file is used to test variables
#To define an integer, use the following syntax:
number = 7
print(number)
#to make the number as floating
number = float(7)
print(number)
string = 'hello'
print(string)
#we can use both single and double quotations
#Assignments can be done on more than one variable "simultaneously" on the same line like this
a,b = 1,2
print(a,b)
mystring = 'hello'
myfloat = 10.0
myint = 20
# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
#f strings can also be used and they are also placeholders
print(f'string is {mystring}')
print(f'integer is {myint}')
print(f'float is {myfloat}')
