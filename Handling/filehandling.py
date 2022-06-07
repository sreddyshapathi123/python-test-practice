##file handling part very important in any web application#
#python has many functins for creating deleteing reading updating files#
#the key function for working with files in python is open() function#
#the open() function takes two parms: filename,and mode#
#we have 4 methods in python(modes)#
#r-a-w-x#
#r-open a file for reading ,get error if file doent exist
#a-append-open a file for appending  ,creates the file if file doesnt exist#
#w-write-open a file for writing create the file ,if doesnt exist#
#x-create- create the sepcified file ,get error if file already exist#

#t-textmode
#b-biary mode

#using open() function#
#f=open("demofile.txt")
#here will get error we are not mentioned mode#


#using with mode and open() function ##

f= open("demofile.txt","at")#here a- appending means creates file ,t means text file#-op-demofile.txt


#using "r" mode#
f=open("demofile.txt","r")#r-means read the file#
print(f.read())


#if we file is different location then  we will specify  the path#
#f=open("D:\\myfiles\demofile.txt","r")
#print(f.read())



#if we want read the 5 charecters from the demofile then##
f=open("demofile.txt","r")
print(f.read(5))#get op-hello#



#if we want to read one line output then# use readline() function##

f=open("demofile.txt","r")
print(f.readline())


#if we calling readline() two times then we can read the data two lines from the file##
f=open("demofile.txt","r")
print(f.readline())
print(f.readline())


#by using the looping the file we can read the file data one by one line#

f=open("demofile.txt","r")
for x in f:
 print(x)



#using close () after reading the file its closing automatically##

f=open("demofile.txt","r")
print(f.readline())
f.close()



#by using "append"-a" mode we can add the data in the  file and save close and read the data from the file##
f=open("demofile.txt","a")
f.write("hi this is sudhakarreddys hapathi")   #here using append mode adding the content to  that file#
f.close()                                      #after saving the data closing the file#
#now we will read the data from file#
f=open("demofile.txt","r")                     #using r-read mode we can read the data from the file#
print(f.read())



#using x-create mode to create the empty file#

#f=open("test.txt","x")#   here commenting the code because if run every time will get error as file exists so##



##delete the file #
#To delete a file, you must import the OS module, and run its os.remove() function:##
import os
os.remove("demofile.txt")
#if the file present then remove the file otherwise get error#


#to avoid the error ,first we need to check the file exist or not if exist then will delete otherwise wwill get popup message##

import os
if os.path.exists("demofile.txt"):
 os.remove("demofile.txt")
else:
 print("the file does not exist")


#delete the folder using os.rmdir() method##

#import os
#os.rmdir("myfolder")      #if folder exist then remove ,other wise will get error#commenting the code#
