#BY using for statement and append()function we can create short items with create new list from the existing list #

fruits = ["mango","kiwi","orange","apple","cherry"]
 #if we want  items with "a" letter itms then#
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


#we can writre in singel piece of code##

fruits = ["mango","kiwi","orange","apple","cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#if we want to print  except selected item then we will use like this##


fruits = ["mango","kiwi","orange","apple","cherry"]
#print all items except apple#
newlist = [x for x in fruits if x != "apple"]
print(newlist)


##creating iterable means set,list,tuple##

#using range()function create iterable##
mylist = [x for x in range(10)]
print(mylist)

#using if condition##
mylist =  [x for x in range(10) if x < 5]
print(mylist)

#change to uppervalues form newlist ietms##
mylist = ["mango","kiwi","orange","apple","cherry"]
mylist = [x.upper() for x in mylist]
print(mylist)



#replace "hello" in all fruits items location##
mylist = ["mango","kiwi","orange","apple","cherry"]
mylist =  ['hello' for x in mylist]
print(mylist)


#replace the value where the item is ##
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#using sort() function ##sort the values alphabitically##

#write the items in alphabitically##

fruits=["mango","apple","orange","apple","kiwi"]
fruits.sort()
print(fruits)

#write numbers ascending  with sort##

numbers = [59,66,89,70,100]
numbers.sort()
print(numbers)

#write case sensitive alphabits give output from capital letters to samll letters items##

fruits = ["Mango","apple","Kiwi","banana"]
fruits.sort()
print(fruits)##give op-Mango,Kiwi,apple.banana#

#write nos with sort descending##
numbers = [59,66,89,70,100]
numbers.sort(reverse=True)
print(numbers)

# write onl;y small leterse first then##
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)


