wishlist =["banana","orange","mango"]
print(wishlist)


wishlist =["banana","orange","mango"]
print(wishlist[1])

#finding how many items in the value#

wishlist =["banana","orange","mango"]
print(len(wishlist))

#string, int, boolean data types#

list1 = ["banana","orange","mango"]
list2 = [1,2,3,4,5]
list3 = [True,False,True,True]
print(list1)
print(list2)
print(list3)

list1=["hello",1,True,False,30,"mango"]
print(list1)


wishlist =["banana","orange","mango"]
print(type(wishlist))

#it ll write  reverse item##

mylist =["banana","orange","mango"]
print(mylist[-1])

#it will write from 2nd ration to 5th ratio#
mylist= ["banana","orange","mango","fruits","apple","kiwi"]
print(mylist[2:5])


##This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):###

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#if fruit is present##
fruits = ["banana","orange","manngo"]
if "orange" in fruits:
    print("yes, 'orange is the fruits list")

    #replacing the fruit in list #
fruits = ["banana","orange","manngo"]
fruits[1]="apple"
print(fruits)

# replace banana and cherry with  this list values#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#change the value of second value with two new values##
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#change the first   value with 3 values#

mylist = ["appple","banana"]
mylist[1]="sudhakar","ssr"
print(mylist)

#if we want to add the item in existing list we ll use append()function#

mylist =["banana","orange"]
mylist.append("mango")
print(mylist)

#if we add an item at specified index location ll use insert()method##
##here 0=banana;1=orange:2=apple## we need to print the mango value at 1 location #we are not replacing the value just we are adding the item##
mylist =["banana","orange","apple"]
mylist.insert(1,"mango")
print(mylist)

#here we can add the items to existing list from othe rlist items using "extend()"function#

mylist =["mango","orange","apple"]
otherlist =["cherry","watermelon","guva"]
mylist.extend(otherlist)
print(mylist)

#add items after end using extend woith tuple items##
mylist =["mango","orange","apple"]
otherlist=("cherry","guva")#tuple items called#
mylist.extend(otherlist)
print(mylist)


## Remove list items ##
#remove item using remove() function##
mylist =  ["mango","orange","banana"]
mylist.remove("mango")
print(mylist)

#remove specified index(item) with po()function##
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#delete entire files usinng entire files #

thislist = ["apple", "banana", "cherry"]
del thislist

#using clear() fnction clear all data##
thislist =["apple","banana","orange"]
thislist.clear()
print(thislist)

#using for loop we can print all items one by one#
mylist = ["apple","banana","orange"]
for x in mylist:
    print(x)

#print all items using their index numbers##
mylist = ["apple","bannaa","mango"]
for i in range(len(mylist)):
    print(mylist[i])

#using while loop ,print items#

mylist = ["apple","bannaa","mango"]
i=0
while i <len(mylist):
    print(mylist[i])
    i=i+1


