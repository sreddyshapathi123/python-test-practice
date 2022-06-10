##iterator is an object  ,its contains a countable number of values#
# in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().##
#here return a iterator value and print each value#
mytuple=("apple","banana","mango")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#using string value#
mystring="apple"
myit=iter(mystring)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



#We can also use a for loop to iterate through an iterable object#
mytuple=("banana","apple","mango")
for x in mytuple:
    print(x)


#Iterate the characters of a string:#

mystring="apple"
for x in mystring:
    print(x)



#create iterator that return numbers and starting with 1 nd each sequence will increase by one##
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):#here sequence increasing by one###using next item it will return next item in sequence
       x=self.a
       self.a +=1
       return x

myclass=MyNumbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#using "stopIteration" statement we can stop the no of iterations#
#here stop after 20 iterations#
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 20:  #if 20 iterations done then #
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration  #stop the iterations#
myclass=mynumbers()
myiter=iter(myclass)

for x in myiter:#here using for loop through ,vcaaling the $myiter$##
    print(x)
