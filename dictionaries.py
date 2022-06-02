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
 details.clear["location"]
print(details)




