##functions is a block of code which only ruyyns when it is called##
#creating python function defied by def keyword##
def myfunction():
    print("hello world")
myfunction()#calling a function#



##arguments##
#info can be pasded into functions as arguments##
def my_function(fname):#with argument#
    print(fname + " sudhakar")#here calling the function an dprint the full names#
my_function("shapathi")#here we passsed first names#
my_function("reddy")
my_function("sr")



#using 2 orgumnets# the function expect 2 arguments then we will call mush nd should call function with 2 arguments not more not less#

def my_function(fname,lname):#here calling two arguments#
    print(fname + " " + lname)
my_function("shapathi", "sudhakar")#function with 2 arguments#




#arbitary arguments#if u want to add number of arguments then add a * before the paraeter name in the function definition##

def my_function(*kids):
    print("the youngest child is  " + kids[3])
my_function("abc","cdf","mnr","klm")



##we can send arguments with the key = values#
def my_function(child3,child2,child1):
     print("the youngest child is " + child3)#here  printing the value of youngest child#
my_function(child1="abc",child2="cdf",child3 ="ssr")



#if we dont know howmany key words are passed to function then add ** to the parameter#
def my_function(**kid):
  print("his last a name" + kid["lname"])
my_function(fname="abc",lname=" shapthi")


#using default  parameter Value#without argument we can use default value##
def my_function(country=" india"):
    print("Iam from" + country)
my_function()#here mentioned key value #
my_function("usa")#here directly called #
my_function("uk")


#we can send any data type arugument inside a function it is consider as same data type inside function##
def my_function(food):
    for x in food:
        print(x)
fruits =["apple","bannaa","cherry"]
my_function(fruits)


#using return statement return a value##
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(8))

#using pass statement we will avoid error#
#function definition cant be empty ,if it is empty then will get error ,by using  pass statement avoid getting error##

def myfunction():
    pass
