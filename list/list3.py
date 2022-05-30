#COPY FUNCTIONS##
#using copy() function copy the data to new file from existing file##

fruits = ["mango", "orange","apple","banana"]
newfruits=fruits.copy()
print(newfruits)

#using list also we can copy the data##

fruits = ["mango", "orange","apple","banana"]
mylist = list(fruits)
print(mylist)

#join lists##

#using list() function we ll add two items##

list1= [1,2,3,4]
list2 = ["a","b","c"]
list3=list1+list2
print(list3)##-op-1,2,3,4,a,b,c

#usinng extend() function also adding items##
list1= [1,2,3,4]
list2 = ["a","b","c"]
list1.extend(list2)
print(list1)
