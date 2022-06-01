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


