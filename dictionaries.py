##DICTIONARIES##
#dictionaries are used to store tha key:value pairs:#
#not allowed duplicates##

details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
print(details)

#@@@@@@@@--Dictionaries allowed changeble and ordered but does nt allowed duplicates##@@@@@@@@2


#only print the name of the person#
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
print(details["name"])

#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.##

#duplicate val;ues overwrite the existing values#
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad",#overwriting place##
    "place" : "bengalur"
}
print(details)


#using len()  method , print number of  items in dictionary##
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
print(len(details))


#using string,int,boolean #

details = {
    "brand" : "apple",
    "value" : "true",
    "price" : "599",
    "colors" : ["red","white","yellow"]
}
print(details)

#data type of dictionary in python defined "class type"##
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
print(type(details))

##Accessing Items##
#we can access the items in dictionary by calling key values##
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
x=details["name"]##calling the value#
print(x)

#using get() method we can call the values##
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
x=details.get("age")
print(x)

##Using key() method w used to if any changes in  original dictionary  then key values automitically updated in dictionary##

details = {
        "name" : "mobile",
        "brand" : "aplpe",
        "color" : "red"
}
x =details.keys()
print(x)#before change#
details["cost"] = 999
print(x)#after the change#
#op-add -cost -999#

##by using values() method  its  return values of dictonary items#
#using values() method  changing the item value before after##

details = {
        "name" : "mobile",
        "brand" :"samsung",
        "color" : "blue"
}
x =details.values()
print(x)#  before items
details["year"] = 1976#adding iitem#
print(x)


#using values() method  changing the item value before after##
details = {
        "name" : "mobile",
        "brand" :"samsung",
        "color" : "blue"
}
x =details.values()
print(x)#  before items
details["color"] = "red"#after changing (replacing) iitem#
print(x)


##item() method use to return the all dictionary items#changing values  before after##
details = {
         "name" : "mobile",
        "brand" :"samsung",
        "color" : "blue"
 
}
x= details.items()#adding all items
print(x)#before  change value
details["color"] = "yellow"
print(x)#after  changing value##

##item() method using adding the new items to dictionary##
details = {
         "name" : "mobile",
        "brand" :"samsung",
        "color" : "blue"
}
x= details.items()#adding all items
print(x)#before  change value
details["year"] = 1995
print(x)#after  changing value##



##using"if" key word will get item present or Not##
details = {
         "name" : "mobile",
        "brand" :"samsung",
        "color" : "blue"
}
if "brand" in details:
    print("yes ' 'the brand value present in details dictionary")


##Change Items##
#changethe item value  by its refering key value##

details = {
        "name" : "sudhakar",
        "place" : "hydrabad",
        "age" : 26
}
details["age"] = "33"
print(details)

#using update() method also  updating the item value###

details = {
        "name" : "sudhakar",
        "place" : "hydrabad",
        "age" : 26
 
}
details.update({"age": 25})
print(details)

##Add Items###
#adding a item using a inew index key by reffering its key value##


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

##Remove dictionary Items##

#using pop() method remove the dictionary items reffred by key values##

details =  {
        "name" : "mobile",
        "brand" : "apple",
        "location" : "USA"
}
details.pop("brand")
print(details)


#using popitem () method if we not mention any item then it will remove last item from the dictionary#
details =  {
        "name" : "mobile",
        "brand" : "apple",
        "location" : "USA"
}
details.popitem()
print(details)

#using "del" key remove items from the dictionary##
details =  {
        "name" : "mobile",
        "brand" : "apple",
        "location" : "USA"
}
del details["brand"]
print(details)

#using del key word remove all items then will  get error##
#details =  {
 #       "name" : "mobile",
  #      "brand" : "apple",
   #     "location" : "USA"
#}
#del details#here deleteing the entire dictionary then how it  is print without dictionry so will get error as "not  difined"
#print(details)

#using clear() method  we will remove dictionary items##
details =  {
        "name" : "mobile",
        "brand" : "apple",
        "location" : "USA"
}
details.clear()
print(details)

##loop dictionaries#
#we can loop through a dictionary by using "for" loop.##
#by using this wwe can return keys of dictionary as wella s values also we hava another method for values##
details = {
        "name" : "sudhakar",
        "age" : 26,
        "place" : "hydrabad"
}
for x in details:
    print(x)

#print all values##
details = {
        "name" : "sudhakar",
        "age" : 26,
        "place" : "hydrabad"
}
for x in details:
    print(details[x])

##BY USING key() method we can return a keys on dictionary#
details = {
        "name" : "sudhakar",
        "age" : 26,
        "place" : "hydrabad"
}
for x in details.keys():
    print(x)

##using values we can return values of dictionary items##

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.values():
    print(x)

#using item() method  we can loop booth keys and values  print#
thisdict =      {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in thisdict.items():
  print(x,y)


##Copy Dictionaries##
#by using copy() method we can copy the dictionary  items##
details = {
        "name" : "sudhakar",
        "age" : 26,
        "place" : "hydrabad"
}
newdetails =details.copy()
print(newdetails)

#another way copy dictionary  with dict() function:##
details = {
        "name" : "Jhon",
        "age" : 55,
        "place" : "USA"
}
newdetails = dict(details)
print(newdetails)

#Nested dictionaries##
#create dictionary that containe 3 or more dictionaries called nested dictionary#
myfamily = {
        "father" : {
            "name" : "john",
            "age" : 55
    },
        "mother" : {
            "name" : "meri",
            "age" : 48
    },
        "Brother" : {
            "name" : "bolward",
            "age" : 24
    }
}
print(myfamily)


#create dictionaries and create one dictionary containes other dictionaries##

child1 =   {
        "name" : "abc",
        "age" : 12
}

child2 = {
        "name" : "def",
        "age" : 11
}

child3 = {
        "name" : "ghi",
        "age" : 14
}

family = {
        "child1" : child1,
        "child2" : child2,
        "child3" :child3
}
print(family)





##====>>>>Dictionary Methods#we are used these all methods###:::<<<<====

###Python has a set of built-in methods that you can use on dictionaries.

#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
p#op()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary
