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
