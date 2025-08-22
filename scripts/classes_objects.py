#learning objects and classes
#class Dog:
    #def __init__(self, name, age):
        #self.name = name
        #self.age =  age

      



    #def bark(self):
        #print("woof!")

#roger = Dog("Roger",8)

#print(roger.name)
#print(roger.age)
#roger.bark()

class Vehicle:
    def __init__(self,name,color,model,worth):
        self.name = name
        self.color = color
        self.model = model
        self.worth = worth
    
    def dscr(self):
        str= f"{self.name} is a {self.color} color {self.model} car. Its current worth in the market is {self.worth}"
        return str
    
car1 = Vehicle('Toyota Corolla','Black','2016','4 million pkr')
car2 = Vehicle('Honda Civic','White','2018','5 million pkr')
car3= Vehicle('Kia Sportage','Red','2020','7 million Pkr')

print(car1.dscr()) #forgot to add () this after dscr so was not working previosuly
print(car2.dscr()) #__init__ is a built in function which can use self and give various attributes to the class
print(car3.dscr()) #we can make different functions in one class, concepts of global and private classes not taught





