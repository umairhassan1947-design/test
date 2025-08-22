#learning functions
def myfunction(): #defining function
    print('hello umair hassan') #content of the function
myfunction() #calling the functions

def sumof2numbers():
    a= int(input('enter a '))
    b= int(input('enter b '))
    output = print(f"sum of a and b is {a+b}") #printing the sum in the function so when function is called sum is done
    return output
sumof2numbers()

#print("sum of both a and b is ", sumof2numbers()) #use this if you want to print seperately

def greetingswithpython():
    name = input('enter your name ')
    age = int(input("Enter your age "))
    major = input('Enter your major ')
    return print(f"Hi {name}, I hope you're doing well. You are {age} years old and are currently doing {major}.")

greetingswithpython()




