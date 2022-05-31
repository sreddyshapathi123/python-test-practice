
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


