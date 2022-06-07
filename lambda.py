##Lambda##
#lambda function can take any no fo aruments but only one expression##
#adding 10 value to argument a and return the result#
x=lambda a:a+10
print(x(6))#a vlue is 6##
##op-16##

#multiply argument a with arugument b##
x=lambda a,b :a*b
print(x(5,6))

#division #argument a with b##
x=lambda a,b : a/b
print(x(20,5))


#adding more arguments a,b,c##
x=lambda a,b,c :a+b-c
print(x(10,5,4))


##using lambda "return" functions##
def my_function(n):              #here calling argument##
    return lambda a :a*n         #using arugument with lambda##
x=my_function(2)                 #calling argument value with some other value#x
print(x(11))                     #print of other value and argument value#






#using same function definition for both functions##

def my_func(n):
    return lambda a:a*n
x=my_func(3)
y=my_func(6)
print(x(7))
print(y(8))


