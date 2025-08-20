#understanding lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) 
print(mylist[1])
print(mylist[2]) 

# prints out 1,2,3
for x in mylist:
    print(x)
#testing lists 
numbers = []
numbers.append(5)
numbers.append(6)
numbers.append(8)
numbers.append(4)
numbers.append(55)
numbers.append(62)
numbers.append(9)
numbers.append(24)
for x in range(0,5) : #range 0 to 5 is used because 0 is the first index in the list and 5-1 is 4 hence 0,1,2,3,4,will come
  print(numbers[x])

#selecting specific items from lists
names = ['umair', 'ali', 'wattoo', 'alu','niazi']
print(f'second name on the list is {names[1]}') #1 is used because index starts from 0
#done


    