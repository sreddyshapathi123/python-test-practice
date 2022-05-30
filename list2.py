#BY using for statement and append()function we can create short items with create new list from the existing list #

fruits = ["mango","kiwi","orange","apple","cherry"]
 #if we want  items with "a" letter itms then#
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


#we can writre in singel piece of code##

fruits = ["mango","kiwi","orange","apple","cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#if we want to print  except selected item then we will use like this##


fruits = ["mango","kiwi","orange","apple","cherry"]
#print all items except apple#
newlist = [x for x in fruits if x != "apple"]
print(newlist)
