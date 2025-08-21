#learning conditions
n = 10
print(n == 10)
print(n == 100)
print(n < 100)

name = input('Enter your name: ')
age = 21
if name == 'umair' and age == 21:
    print('your name is umair and you are 21 years old')
else:
    print('lololol')

if name in ['umair', 'umar']: #looks for umair or umar in the variable name
    print('your name is umair or umar')
else:
    print('lolol')

x = [1,2,3]
y = [1,2,3]
print(x==y) # compares values
print(x is y) # looks for whether the instance memory is same or not, basically x needs to be y 

