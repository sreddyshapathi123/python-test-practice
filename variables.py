#basic hello world output#

print("Hello, World!")

#python indentationbelow its correct indentation#

if 5 > 2:
  print("Five is greater than two!")

  #syntax error#
# if 5 > 2:
# print("Five is greater than two!")

#indentation#

if 5 > 3:
     print("five greater than 3")
if 5 < 3:
    print("five less than 3")
#use variables#
x= 5
y= "hello world"
print (x)
print(y)

#using variables and data types #

#If you want to specify the data type of a variable, this can be done with casting.#

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#finding data type using varaibles values#

x=5
y="sudhakar"
print(type(x))
print(type(y))

#we can use double or single quotes for string variables below ##

x="sudhakar"
y='ssr'
print(x)
print(y)

#we can use small and captial alphabits these are not overwrite below ex:#

a="sudhakar"
A='sudha'
print(a)
print(A)

#we can use names as varaibales#
#but the names start with only letter either small or capital or underscoore but not with number#
#name contain with alphanumaric with underscore#

myvar="john"
_myvar='sudhakar'
my_var='ssr'
Myvar='sbr'
MYVAR='MNR'
_my_var='swet'

print(myvar)
print(_myvar)
print(MYVAR)
print(_my_var)
print(Myvar)

#multiple values with multiple variables#

x,y,z = "orange","apple","banana"

print(x)
print(y)
print(z)

#same value with multiple variables#


x=y=z= "orange","apple","banana"
print(x)
print(y)
print(z)

x=y=z= "orange"
print(x)
print(y)
print(z)

#unpacking the package using variables#

fruits=("orange","apple","banana")
x=y=z=fruits
print(x)
print(y)
print(z)

#we will use multiple variables in print() function output#
x='jhon'
y='mari'
z='adern'
print(x,y,z)     #by using commas we can separate them#

  #or we can using plus symbol to separate#
x='jhon2 '
y='mari2 '
z='adern2 '
print(x+y+z)

#create a variable outsiide of the function and use in inside of the function#

x="awesome"

def myfunc():
  print("python is " + x)
myfunc()

#ex2:

x=y=z="hello world"
def myfunc():
    print("hi this is " +x+y+z)
myfunc()

#if the  variable value mentioned in out side and inside of the function the inside varible call the inside value and outside variobale call the out side value or global value##

x= "hi ssr"
def myfunc():
    x= "hi this is sudhahkar reddys hapathi "
    print("hey " +x)
myfunc() 
print("hello " +x)

#python numbers#

x= "hello world"
y= 5
z= 5.9
a= 1j
print(type(x))
print(type(y))
print(type(z))
print(type(a))

#variable casting#
x=int(2)
y=int(2.0)
z=int(2.88)
print(x)
print(y)
print(z)

