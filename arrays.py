##pythonn use arrays with only list types##
#arrays are used to store the multiple values in single variable#

#create array with car names#
cars=["ford","baleno","xuv"]
print(cars)



#array can hold more than one value at a  time##
#get the first array item from array list#
cars=["ford","baleno","xuv"]
x=cars[0]
print(x)


#modify the value of first array item#

cars=["ford","baleno","xuv"]
cars[0]="innova"#replace value at first array item#op-innova  baleno.xuv##
print(cars)

#using len() function in arrays##
cars=["ford","baleno","xuv"]
print(len(cars))
 ##or we can write like this #
cars=["ford","baleno","xuv"]
x=len(cars)
print(x)



#using for loop in arrays##
cars=["ford","baleno","xuv"]
for x in cars:
    print(x


            )

#using append() method adding array elements#

cars=["ford","baleno","xuv"]
cars.append("creta")
print(cars)



##we can use pop() or remove() method for removing the  array elements##
cars=["ford","baleno","xuv"]
cars.pop(0)#calling by  index number#
print(cars)


#using remove () method##
cars=["ford","baleno","xuv"]
cars.remove("baleno")#here using value to remove the array element#
print(cars)


##Array Methods

#Python has a set of built-in methods that you can use on lists/arrays.

#append()	Adding element at end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
