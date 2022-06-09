#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class, also called derived class.

#create parent class# any class bea parent class#

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):#here using printname()method#
           print(self.firstname,self.lastname)

    #use the person class to create an object,then will excute printname method#

x=person("ssr","shapathi")
x.printname()

#create child class# child class inherit form anotther class#
class student(person):#here person is the another class
    pass
######create child class by using parent class data#

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(person):               #child class inheriting form parent class #
    pass                             #if we dont want to  add nay properties /methods to the class then will use "pass"keyword
x= Student("sudhakar","shapathi")    #here using child  class for creating object
x.printname()                        #printing the value#



############classes/objects##
class person:
  def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
p1=person("sudhakar",22,"hyd")

print(p1.name)
print(p1.age)
print(p1.place)





# No w we ll add the" __init ()" function add to the child class instead of "pass" keyword##
#if we add the "init()" function to child class ,then the child class will not inheritance  from the parent class#
#child class override the parent class#

class person:
    def __init__(self, fname,lname):

        self.firstname=fname
        self.lastname=lname
    def printname(self):
       print(self.firstname,self.lastname)

class student(person):                          
    def __init__(self,fname,lname):       #child class overriding the parent class#
      person.__init__(self,fname,lname)
x=student("sudhakar","shapathi")
x.printname()





#BY using "super()" function we can inherit all methods and prooperties from the parent class##

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init(fname,lname):
        super().__init__(self,fname,lname)#using super () function##
x=student("sweet","shapathi")
x.printname()




#using graduationyear for student##
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastnamee=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname):
     super().__init__(fname,lname)
     self.graduationyear=2016   #here year we are passing variable(2016) to student class yhen create student obejcts##
x=student("sudhakarreddy","shapathi")
print(x.graduationyear)





##now we will add year paramater and pass the correct year when creatng objects#

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
x=student("sudhakar","shapathi",2020)
print(x.graduationyear)




#if we add the one more def method in child class as a same function then the  inheritance of parent class will be overridden##

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of ", self.graduationyear)
x=student("sudhakarreddy","shapathi",2016)
x.welcome()



