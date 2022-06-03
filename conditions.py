##if statement##
#in python support several ways logical conditions##

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
#Greater than: a > b
# Greater than or equal to: a >= b
#########################################

#if statement #

a=20
b=30
if a<b:
    print("a is less than b")

#using elseif and if  statement##
a=200
b=300
if a>b:
    print("a greater than b")
elif a<b:
    print("a less than b")

#using "if",elseif","else" statements##
a= 100
b=200
if a>b:
    print("a greater than b")
elif a==b:
    print("a equal to b")
else:
    print("a less than b")
#we can write if and else instead of elif##
a= 100
b=200
if a>b:
    print("a greater than b")
else:
    print("b greater than a")

#one line statement using "if"#
if a<b:print("a less than b")

#write one line statement using "if else "##
a=23
b=34
print("a less than b") if a<b else print("no")

#here we can use multiple statements##
a=200
b=200
print("a less than b") if a<b else print("=") if a==b else print("b")
#here will get op-"="##


#using + operator combining both conditions##
a=200
b=300
c=400
if a<b and c>b:
    print("both coditons are true")

##using or oeprator combine two statements##
a=200
b=30
c=500
if a>b or a==b:
    print("atleast one statement is TRue")
##Nested If #if statement and inside the iof stament again if statement called "nested if "##

a=50
if a>10:
     print("print ten")
     if a>20:
         print("print twenty")
     else:
         print("donnt print twenty")

#in if statement without contente will get eror by using pass statement we can put if statemnt without any content##

a = 200
b = 300

if b > a:
  pass
