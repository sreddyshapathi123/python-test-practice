
##PYTHON TUPLES##
#Tuples are used to store multiple items in single variable##

mytuple = ("apple","banana","orange")
print(mytuple)

#tuples allowed duplicates#
mytuple = ("apple","banana","orange","apple")
print(mytuple)

#Using len()function find lenght of the tuple items##
mytuple = ("apple","banana","orange")
print(len(mytuple))

#creating single tuple item ,tuple mentioned with comma#

mytuple =("apple",)
print(type(mytuple))

#Not a tuple##

mytuple =("apple")
print(type(mytuple))



#stringand boolean @int data types#

tuple1 = ("apple","banana","cherry")
tuple2 =  (1,3,5,4,6)
tuple3 = (True,False,False)

print(tuple1)
print(tuple2)
print(tuple3)

##finding data types of items##
tuple1 = ("apple","banana","cherry")
tuple2 =  (1,3,5,4,6)
tuple3 = (True,False,False)

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

##ACCESS TUPLE ITEMS##

#print the second item from the tuple##
mytuple = ("apple","banana","cherry")
print(mytuple[1]) #index =0-apple,1-banana-2-cherry##

#negative index means start from end #-1 reffres to cherry ,-2 reffres banana##
mytuple = ("apple","banana","cherry")
print(mytuple[-1])

#here we are specifying range from the tuple##
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#here 2 included but 5 value not included#

##this example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

##This example returns the items from "cherry" and to the end:##
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

##This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#here will get o-p =melon,kiwi,orange

#using if condition #check apple present in tuple#

mytuple = ("apple","orange","mango")
if "apple" in mytuple:
    print("yes,' apple in mytuple list")


##UPDATE TUPLES##


#here we cant change values in tuple so we ll covert tuple into list then change the value##
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" #here we are replacing kiwi value at index -1(banana)##
x = tuple(y)

print(x)

#TUPLES ARE IMMUTABLE SO ,DONT HAVE APPEND() function so need to convert tuple to list and use append() function##

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)##converting to list#
y.append("orange")#adding item  to thistuple using with append() function#
thistuple = tuple(y)

##we can add items in tuple using tuple to tuple we can add items##
mytuple =("orange","mango","apple")
y =("kiwi","melon")#we are adding items to the mytuple#
mytuple += y
print(mytuple)


#removing items using list ##

mytuple =("orange","mango","apple")
y=list(mytuple)#converting to  list#
y.remove("orange")#removing item#
mytuple =tuple(y)#converting  to tuple#
print(mytuple)

##UNPACK TUPLES##

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits #here assigning values#

print(green)# green=apple,yellow=banana,red=cherry#
print(yellow)
print(red)#op-apple,banana,cherry



#asterisk using#here we ll provide must nfd should no of variables equal to no of values if variables less than values then we will use "*" (asterisk)##

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #green=apple
print(yellow)#yellow=banana
print(red)#remaining fruits should be considered  values for red variable##


#here python assigned values  based on variables here green=apple  red= cherry and remaining 3 valued assigned to "tropic"variable # here asterisk added to the tropic variable##

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

##LOOP TUPLE##
#here we can loop through the tuple items using for loop##
mytuple =("apple","orange","mango")
for x in mytuple:
    print(x)


#using len() range() function we can find index numbers##
mytuple =("guva","sweet","sugar")
for x in range(len(mytuple)):
   print(mytuple[x])

##using while loop#Print all items, using a while loop to go through all the index numbers:##
mytuple =("coc","pepsi","thumsup")
i=0
while i <len(mytuple):
    print(mytuple[i])#print i value
    i= i+1 #here incresing index numbers and print as per values#


##JOIN TUPLES##

#by using + operator we can add 2 or more tuples.###

tuple1 =("a","b","c")
tuple2 = (1,2,3,4)
tuple3 = tuple1+tuple2
print(tuple3)

#using *(multiplication)operator#

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


#Tuple Methods:::::

#Python has two built-in methods that you can use on tuples.

#1)count()	Returns the number of times a specified value occurs in a tuple
#2)index()	Searches the tuple for a specified value and returns the position of where it was found...##
