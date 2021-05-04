# -*- coding: utf-8 -*-
"""
#5 Ways to Swap Two Variables in Python

* Tutorial: https://news.towardsai.net/hnk
* Github: https://github.com/towardsai/tutorials/tree/master/programming
"""

#Using Naive Approach to Swap Values in Python:

def swap_values(x,y):
  #Printing Original Values:
  print("Original Values")
  print("X:",x)
  print("Y:",y)
  print("---------------")

  #Swapping Values:
  temp = x
  x = y
  y = temp

  #Printing Values after Swapping:
  print("Values after Swapping")
  print("X:",x)
  print("Y:",y)

#Function Call:

#Integer Values:
swap_values(10,20)
print("\n")

#Float Values:
swap_values(10.5,20.5)
print("\n")

#String Values:
swap_values("Pratik","Shukla")

#Using comma operator to Swap Values in Python:

def swap_values(x,y):
  #Printing Original Values:
  print("Original Values")
  print("X:",x)
  print("Y:",y)
  print("---------------")

  #Swapping Values:
  x,y = y,x

  #Printing Values after Swapping:
  print("Values after Swapping")
  print("X:",x)
  print("Y:",y)

#Function Call:

#Integer Values:
swap_values(10,20)
print("\n")

#Float Values:
swap_values(10.5,20.5)
print("\n")

#String Values:
swap_values("Pratik","Shukla")

#Using Arithmatic Operator to Swap Values in Python:

def swap_values(x,y):
  #Printing Original Values:
  print("Original Values")
  print("X:",x)
  print("Y:",y)
  print("---------------")

  #Swapping Values:
  x = x+y
  y = x-y
  x = x-y

  #Printing Values after Swapping:
  print("Values after Swapping")
  print("X:",x)
  print("Y:",y)

#Function Call:

#Integer Values:
swap_values(10,20)
print("\n")

#Float Values:
swap_values(10.5,20.5)
print("\n")

#String Values:
#It doesn't work with Strings as it uses numerical operators.
#swap_values("Pratik","Shukla")

#Using Arithmatic Operator to Swap Values in Python:

def swap_values(x,y):
  #Printing Original Values:
  print("Original Values")
  print("X:",x)
  print("Y:",y)
  print("---------------")

  #Swapping Values:
  x = x*y
  y = x/y
  x = x/y

  #Printing Values after Swapping:
  print("Values after Swapping")
  print("X:",x)
  print("Y:",y)

#Function Call:

#Integer Values:
swap_values(10,20)
print("\n")

#Float Values:
swap_values(10.5,20.5)
print("\n")

#String Values:
#It doesn't work with Strings as it uses numerical operators.
#swap_values("Pratik","Shukla")

#Using Arithmatic Operator to Swap Values in Python:

def swap_values(x,y):
  #Printing Original Values:
  print("Original Values")
  print("X:",x)
  print("Y:",y)
  print("---------------")

  #Swapping Values:
  x = x^y
  y = x^y
  x = x^y

  #Printing Values after Swapping:
  print("Values after Swapping")
  print("X:",x)
  print("Y:",y)

#Function Call:

#Integer Values:
swap_values(10,20)
print("\n")

#Float Values:
#It only works with integers.
#swap_values(10.5,20.5)

#String Values:
#It doesn't work with Strings as it uses numerical operators.
#swap_values("Pratik","Shukla")
