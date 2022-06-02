##DICTIONARIES##
#dictionaries are used to store tha key:value pairs:#
#not allowed duplicates##

details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
print(details)


#dictionaries allowed changeble and ordered but does nt allowed duplicates##
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


#using len() print no items in dictionary##
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
x=details["name"]
print(x)

#using get() method we can call the values##
details = {
    "name" : "sudhakar",
    "age" : 26,
    "place" : "hydrabad"
}
x=details.get("age")
print(x)


