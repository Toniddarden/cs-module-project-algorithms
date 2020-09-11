#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    items = []
    capacity = sum(items, 0)
    n_items = int(input('Enter in your treasures value: '))
    # item_1 = input("Enter in your first treasure value: ")
    # item_2 = input("Enter in your second treasure value: ")
    # item_3 = input("Enter in your third treasure value: ")
      # value = (input())
      # items.append(value)
    # for n in items:
    # base case 
    # **** for every item inputed, 
    for x in range(0, n_items, -1):
        # **** if that item is over(greater) than the capacity .pop() that item off 
        if x > capacity:
          items.pop(x)
        # **** if that item is under capacity, add it to the items list 
        elif x < capacity:
          items.append(x)
        else:
          return print('please enter another value')
    
    total_val = Item(items)
    print(total_val) 

    # pass


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
    
    
# Ex. 1 lecture example **************************************
# Given the radius of a circle, calculate it's area and and format
# the result to three decimal places

# A = PI * r^2
# use extract value of PI
# format output as a string 
import math
def area_circle(radius):
    # do math to calculate the "area"
    area = math.pi * (radius * radius)
    # format the result 
    result = f'{area:.3f}'
    # return result 
    return result
  

  
  
print(area_circle(3))   # 28.274
# Ex. 2
# We'll say that a positive int divides itself if every digit in the 
# number divides into the number evenly. So for example 128 divides 
# itself since 1, 2, and 8 all divide into 128 evenly. 
# And we'll say that 0 does not divide into anything evenly, so no 
# number with a 0 digit divides itself. 
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]
def divides_self(num):
  # copy num
  digits_left = num
  # loop throug all digits in num
  while digits_left > 0:
    # num % 10 to GET the digit on the RHS
    digit = digits_left % 10
    # if that result a 0, return false 
    if digit == 0:
      return False 
    # if num % result is NOT 0, return false 
    if num % digit != 0:
      return False 
    # // 10 to chop off the digit on the RHS 
    digits_left = digits_left // 10
  # else return true 
  else:
    return True

    pass
print(divides_self(128)) # → True
print(divides_self(12)) # → True
print(divides_self(120)) # → False
print(divides_self(152)) # → False
# Ex. 3
# The Knapsack Problem
# https://en.wikipedia.org/wiki/Knapsack_problem