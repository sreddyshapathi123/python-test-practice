import modules
modules.greeting("ssr")



#here using  module will call the person details in that module file##

import modules
a=modules.person1["age"]    #here calling the age of  the person1#
print(a)                  #accessing the details from person 1 dectionary in (modules.py) file#


#we can create a alias  when we are importing a module using "as" ketword##

import modules as mx
a=mx.person1["name"]
print(a)



##impport module using "platform" module#

import platform

x = platform.system()
print(x)
##-op-Linux



#using dir() function it ios containing all variables and names  already build in this function##

import platform
x= dir(platform)
print(x)


##using from key word we can import the some parts from the module#(check in modules.py file)

from modules import person1

print(person1["name"])
