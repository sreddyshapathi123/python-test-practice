##Dates#
#a date in python is a own data type ,we can import a module  named "datetime" to work with dats as date obejcts##

#import the datetime module and find the current date#

import datetime 
x=datetime.datetime.now()
print(x)


#return the year and name of weekday#

import datetime 
x=datetime.datetime.now()

print(x.year)            #here we can write month also#will get which month -6 th#
print(x.strftime("%A"))


##to Create a date ,we can use the datetime() clas (constructor)of the datetime module#
#the datetime() class requires 3 parameters to create date,month year#


import datetime

x=datetime.datetime(2020,6,13)
print(x)




#strftime()##
##the datetime obejct has a method for formatting date objects into readable strings##
#the method is called strftime() and takes one parameter  format to specify to retruna string#



#display the name of the month#

import datetime
x= datetime.datetime(2022,6,13)
print(x.strftime("%B"))


#find week day in short#
import datetime
x=datetime.datetime.now()
print(x.strftime("%a")) #will get op -"mon"

#full  version of weekday name##
import datetime
x=datetime.datetime.now()

print(x.strftime("%A"))



#find weekday number0-6##
import datetime
x=datetime.datetime.now()

print(x.strftime("%w"))



#find day of the month 1-31st#
import datetime
x=datetime.datetime.now()

print(x.strftime("%d"))


##month name short version#
import datetime
x=datetime.datetime.now()

print(x.strftime("%b"))



#month name full version##

import datetime
x=datetime.datetime.now()

print(x.strftime("%B"))




#month as a number -1-12 months##
import datetime
x=datetime.datetime.now()

print(x.strftime("%m"))



#year shorcut without century##

import datetime
x=datetime.datetime.now()

print(x.strftime("%y"))


#year full version#

import datetime
x=datetime.datetime.now()

print(x.strftime("%a"))




#find 24 hours format ##
import datetime
x=datetime.datetime.now()

print(x.strftime("%H"))


#find 1 2hours format##
import datetime
x=datetime.datetime.now()

print(x.strftime("%l"))




#find AM/PM#

import datetime
x=datetime.datetime.now()

print(x.strftime("%p"))



#minuts#
import datetime
x=datetime.datetime.now()

print(x.strftime("%M"))




#Seconds##
import datetime
x=datetime.datetime.now()

print(x.strftime("%S"))




#finding no of day in this year 1-366#
import datetime
x=datetime.datetime.now()

print(x.strftime("%j"))



##local version of date nd time#
import datetime
x=datetime.datetime.now()

print(x.strftime("%c"))




#local version of date#
import datetime
x=datetime.datetime.now()

print(x.strftime("%x"))




#local version of time##
import datetime
x=datetime.datetime.now()

print(x.strftime("%X"))



























