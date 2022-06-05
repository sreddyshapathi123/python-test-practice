#if statement####
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


#python while loops##
#by using while loop we can excute set of statements if condition is true##

i=1#variable 1#
while i<8:
    print(i)
    i+=1


#by using break statement we can stop the loop ,if even condition true##
i=1
while i<8:#condition is true(i less than 8)
    print(i)
    if i==3:#i value equal to 3#
        break
    i+=1


#using continue statemnet we can stop current iteration and contuinue with next##
i=0
while i<8:
    i+=1#here loop upto 2 variable#
    if i==3:#if equal 3 then stop at 2 variable#
        continue#using this statement the loop jump to next variable#
    #start with 4 variable#
    print(i)


##using else statement#print the  message once condition is false ##
i=1
while i<6:
 print(i)
 i+=1#upto 5 number printed#
else:
  print("i value is less than 6")

#For loops##
#a for loop is used to iteration over a sequence (that is  list ,tuple,dict,set,str)
#by uising for loop we cna execute set of statements ,once for each item in list,tuple or str,dict etc#

fruits = ("apple","mango","banana")
for x in fruits:
    print(x)

#looping through a string#

for x in "banana":
    print(x)#here will get op-banana words one by one##

#uinsg break statement we can stop the loop#(and before stopping the loop print all items)##
fruits = ["apple","banana","mango","kiwi"]
for x in fruits:
    print(x)
    if x== "mango":
      break#her will get op-upto mango item#



##exit the loop when x in mango ,here break comes before the print##

fruits = ["apple","banana","mango","kiwi"]
for x in fruits:
  if x == "mango":
      break 
  print(x)##herw will get op-upto banana only##



##usingg continue statement we can continue with next item##

fruits = ["apple","banana","mango","kiwi"]
for x in fruits:
  if x == "mango":
      continue
  print(x)##here op-apple,banana,kiwi#




#using range() function we can excecute the code no fo time by mention the no of times  with range function##

for x in range(6):
    print(x)



#using parameters wwe can print the values from  what we can provide  the number for ex(2,6) here print the values form 2 to 6(not include 6 number only upto 5)

for x in range(2,6):
    print(x)




#using third parameter we add the sequence in the number s here(2,30,3) here third parameter menas form 2 to 30 incerement sequemce with 3# 5,8,11, etc...#

for x in range(2,30,3):
    print(x)



#using else  keyword ,when the loop is completed ,then the else statement will printed#

for x in range(6):
    print(x)#here numbers print upto 5 #
else:#here print the bel;ow statement after printing the numbers#
    print("numbers loop completed")



#the else statemnet will not executed if we stopped loop by using break statement##

for x in range(8):
 if x==5: 
   break
 print(x)#here print only upto 4 numbers#
else:
 print("else statemnnt will not executed")



#netsted loops#means nested loop  is a loop inside a loop claaed #nested loops#

adj = ["red", "big", "tasty"]#here print the each adjectibve for every fruit#
fruits = ["apple", "banana", "guva"]

for x in adj:
  for y in fruits:
    print(x, y)
