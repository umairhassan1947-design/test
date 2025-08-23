#learning dictionaries
phonebook = {"umair": 3214820988,"arslan":3099537822,"ali":3214826956,"rumman":3410777766}
phonebook['ahmed'] = 3080044558

def printphonebook():
    for x,y in phonebook.items():
        print(f"The phone number of {x} is {y}.")

printphonebook()


del phonebook["ali"]
phonebook.pop("ahmed")

printphonebook()

#in dictionaries we have a key and a value assigned to that key. key is str and value is in number. 
#its like an array but it has a key and a value and data is stores in it
#we learnt how to delete items from dictionaries
#also how to print from a dictionary in a loop

