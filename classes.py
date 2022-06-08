##classes/Objects##
#class is a obejct cosntructor or "blueprinnt" for creating obejcts#

class myclass:#here creating class name and creating property name--x#
    x=5
print(myclass)

#if we print the value of x then we need to create obejct:

class myclass:
    x=6
p1=myclass()#here created obejct -p1#
print(p1.x)#printing the value of x#


#Use the __init__() function to assign values to object properties#
class person:                    #creating class#
    def __init__(self,name,age): #using init function#
        self.name=name
        self.age =age

p1=person("john",26)             #creating object#

print(p1.name)                  #print the values
print(p1.age)



#objects contained also methods using method #
class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def myfunc(self):#calling the function here#
        print("hi my name is " + self.name)

p1=person("sudhakar",26)
p1.myfunc()



class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
p1=person("ssr",22)
print(p1.name)
print(p1.age)



class person:
    def __init__(self,name,age,place):
     self.name=name
     self.age=age
     self.place=place

p1=person("ssssr",22,"hyd")
print(p1.name)
print(p1.place)
print(p1.age)


##########
class person:
    def  __init__(self,name,age,place):
     self.name=name
     self.age=age
     self.place=place

    def myfunc(self):
        print("hello my name is " + self.name)
p1=person("sbr",55,"hyd")
p1.myfunc()



#self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.##

class person:
    def __init__(subject,name,age,place):
      subject.name=name
      subject.age=age
      subject.place=place
    def myfunc(abc):       #here calling   self  parameter and calls only name of the value##
        print("hi my name is " + abc.name)

p1=person("jhon","23","usa")
p1.myfunc()                    #/op-hi my name is jhon#



#we can modify the properties#
class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def myfunc(self):
      print("my name is " + self.name)
p1=person("jhn",30)
p1.age =50
print(p1.age)


#using del  keyword##

#class person:
    #def __init__(self,name,age):
    #    self.name=name
   #     self.age=age
  #  def myfunc(self):
 #      print("hi i am  " + self.name)
#p1=person("sbr",55)
#del p1.age
#print(p1.age)-here getting error we are  deleted age obejct#






