#SETS##
#sets are used to store multiple itemsi in single varibale##

myset = {"apple","banana","apple"}#here sets are not allowed duplicate values
print(myset)#op-apple,banana##

#and sets are unchangeable once sets are created ##


#using len() function find no index in sets##

myset = {"apple","banana","cherry"}
print(len(myset))


#a set can be different data types@string,int,boolean##
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


##A set with strings, integers and boolean values:##
set1 = {"abc", 34, True, 40, "male"} 
print(set1)


#data type of set##python defined its class set data type##
myset = {"apple","banana","cherry"}
print(type(myset))

#by using set() constructor make it as set #using double brackets##
myset = (("apple","banana","cherry"))
print(myset)

#access items##
#You cannot access items in a set by referring to an index or a key.#
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword##

myset = {"apple","banana","cherry"}
for x in myset:
    print(x)

#check if banana is present inset##
myset = {"apple","banana","cherry"}
print("banana" in myset)
#once set is created we cant change the items but we can add new items##

##add item##
#use add() function to add the item to the set##
myset = {"apple","banana","cherry"}
myset.add("orange")
print(myset)

#add the items from another set to current set by using upadte() method.##
myset = {"apple","banana","cherry"}
newset = {"orange","mango","kiwi"}
myset.update(newset)
print(myset)

#WE CAN USE ITERABLE (TUPLE,list,dictionaries)these are add to set  by using update() method##
myset = {"apple","banana","cherry"}
newset = ["melon","mango","kiwi"]#these all are list items##
myset.update(newset)
print(myset)

#remove the set item using remove() or discard() method##
myset = {"apple","banana","cherry"}
myset.remove("apple")
print(myset)
  ##or discard() method##
myset = {"apple","banana","cherry"}
myset.discard("banana")
print(myset)


#here we can remopve set items by using pop() method also but pop method is remove ##
myset = {"apple", "banana", "cherry"}

x = myset.pop()#using method##

print(x)##removinng item#

print(myset)#after removing item print##
#above actually popu function which item remove we dont know because of items or inordered so,###


#using clear() method clear the items##
myset = {"apple","banana","cherry"}
myset.clear()
print(myset)

#"delete"  keyword  using delete the set items#
#myset = {"apple","banana","cherry"}
#del myset
#print(myset)#actually here will get error beacuse here given delete command after deleting cant print the myset items##

##You can loop through the set items by using a for loop##:
myset = {"apple","banana","cherry"}
for x in myset:
    print(x)

##JOIN SETS##
#there are many ways to join two or more set items in python we can use uninon() and update() methods for joining the set items##

myset = {"apple","banana","cherry"}
myset2 ={1,2,3,4}
myset3 =myset.union(myset2)
print(myset3)

#using update() method join two set items##
myset = {"a","b","c"}
myset2 ={1,2,3,4}
myset.update(myset2)
print(myset)

#we can print only deplicates on the both items by using intersection_update() method#
x= {"apple","banana","kiwi"}
y= {"apple","melon","guva","kiwi"}
x.intersection_update(y)
print(x)


##The intersection() method will return a new set, that only contains the items that are present in both sets.##
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

##The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

##The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.##
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
