
#string with double quotes#
x="hello"
print(x)

#string wioth single quotes#
x='hello world'
print(x)


#string with three double quotes or three single quotes#

x="""hi this is sudhakarreddys hapathi,im form hydrabad im staying in chengicherla from past four years."""

print(x)


x='''hi this is sudhakar from hydrabad'''
print(x)

##by using slice strings #

x="hello world"
print(x[2:5])     #here we are finding words 2from 2 position to 5 postion from the x value (will get outpu=llo)##


#get the charecters from start to position 5#

x="sudhakar"
print(x[:5])

#if start from 2nd charecter  positin to end will get form  2nd charecter to all worlds##

x="sudhakar shapathi"
print(x[2:])


#Negative indexing#
##here we need postion form (-5) menas we will look form reverse at postion of 2 nd word##

x="hello world!"
#here 2nd postion menas (world!) and from -5 means  form start (!) to end word.
#but not include (o) #
print(x[-5:-2])

#modify strings##

#1.upper cases#
x= "hello, world"
print(x.upper())

#2.Lower case#
x= "HELLO, WORLD"
print(x.lower())

#3.Replace strings#

x= "Hello, world"
print(x.replace("abc", "cdf"))

#4.strip string for removing white spaces before and after the words#

x= " hello, world "
print(x.strip())

#5.split string it s  describe the text#\
x= "Hello, World"
print(x.split(","))#it will write above x values 

#concatenation strings #adding two string values by using + opeeratior##
a = "abhi"
b = "World"
c = a+b
print(c)
#op:abhiworld

#if we want space b/w the words

a = "abhi"
b = "World"
c = a+" " +b
print(c)

#as we learned in varibles we cant  combine number and string using varibales#
#By using format we can combine no and string#

age = 26
x ="my age is {}"
print(x.format(age))


name = 'sudhakar'
age = 26
place = 'hydrabad'
location = 'chengicherla'
details = "hi my name is {0} and my age is {1} i am from {2} present staying in {3}"
print(details.format(name, age, place, location))

#by using escape string we can use double quotes inside the doublequotes#

txt = "hello im sudhakar \"from\" hydrabad "
print(txt)

txt= "hello\tworld"
print(txt)

txt ="hello\rworld"
print(txt)

txt= "hello\bworld"
print(txt)

txt= "hello\nworld"
print(txt)

txt= "hello\fworld"
print(txt)

#uppercase#
txt="hello, world"
print(txt.capitalize())

#strings are arrays finding word from value#

a ="hello world"
print(a[1])

#using for loop#
for x in "banana":
  print(x)

#find no of words using len  string#
  a= 'hello world'
  print(len(a))


