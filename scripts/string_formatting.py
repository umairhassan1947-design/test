#learning string formatting
name = 'umair'
print('hello %s' % name) #we used % method here for place holder
print(f"hello {'hassan'}") # we used f string here to create a place holder and wrote directly in curly

# If we have a variable that we want to call in our output then % placeholder are better but if we want to create a new function or variable then f string is better

name = 'umair'
age = 21
print("%s is %d years old" % (name, age)) #used % method
print(f"{name} is {age} years old") #used f string

data = ("umair","hassan",7500.75)
format_string = "Mr. %s %s has $%f in his account balance."
print(format_string %data)  

s = "hello my name is Umair Hassan!"
print(len(s)) #gives the length of the string s
print(s.index('m')) #gives the index number where first instance of m is found
print(s.count('l')) #gives the count of l in the string
print(s[3:10:2]) #starts from index 3 and goes till 9 with a step of 2 
print (s[::-1]) #reverses the string
print(s.upper()) #converts in uppercase
print(s.lower()) #converts in lowercase









