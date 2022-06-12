#SCOPES#
#a variable is only available from inside the region called created this called as scope#



#cariable ccreated inside a function#

def myfunc():
    x=500
    print(x)
myfunc()     



#create varibale inside a function and access the variable  isidie a function within a function##

def myfunnc():
    x=200
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()



#create variable in outside of the function called its a global variable##

x=300
def myfunc():
    print(x)

myfunc()
print(x)


#create two variables globale one,and inside a function ,python treated as twio diffferent variables#

x=900            #global variable3
def myfunc():     #function#:
    x=800        #varibale inside a function#
    print(x)     #print the inside a function variable#
myfunc()         #callinng iside a function#
print(x)         #out side global variable prinnting#
                  #here  python first call the inside a variable after global 
                     # variable#




#if use global key word t,even that variable inside a fuction that variable as global variable##3

def myfunc():
    global x
    x=350
    print(x)
myfunc()



#want to change global variable value in  inside a function  using  "global" keyword#

x=300            #here given global variable value is 3000#
def myfunc():    #by using global keyword replacing the value of 280 #
    global x
    x=280
    
myfunc()
print(x)




