# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:15:52 2024

@author: RiditaAli
"""

###https://www.freecodecamp.org/news/python-coding-challenges-for-beginners/#python-challenge-3-loves-me-loves-me-not


###Some solutions are from Datacamp and some are created and checked with Datacamp solutions

import pandas as pd
import numpy as np
import math

###Python Challenge #1: Check if a List is Sorted
###The challenge: Write a function that checks whether a given list of numbers is sorted in either ascending or descending order.

listgiven = []

def sort_func(listgiven):
    asc, desc = True, True
    for i in range(len(listgiven) - 1):
        if listgiven[i] > listgiven[i + 1]:
            asc = False
    print(np.sort(listgiven))
    for i in range(len(listgiven) - 1):
        if listgiven[i] < listgiven[i + 1]:
            desc = False
    print('sorted')        
    return asc or desc  
    
#To test the code:

x = [5, 6, 8, 2, 5, 9, 7] #unsorted list
y = [1, 2, 3] #sorted list
    
sort_func(x)            
sort_func(y)


###Python Challenge #2: Convert Binary Numbers to Decimal
###The challenge: Write a function that converts a binary number to its decimal equivalent.

def conv_bin(number):  
    binary = bin(number)
    print('Binary: ', binary)
    print('Decimal: ', float(int(binary, 2)))

#To test the code:
    
conv_bin(7) #any digit / number will be converted to binary format then to decimal format


###Python Challenge #3: Loves Me, Loves Me Not
###The challenge: Given an integer n, print a string that alternates between the phrases "Loves me" and "Loves me not" for each number from 1 to n.

sentence1 = 'Loves me'
sentence2 = 'Loves me not'
  
# Using loop to print elements in criss-cross manner

def phrases(n):
    disp = []
    for i in range(1, n+1):
        if i % 2 != 0:
            disp.append(sentence1)
        else:
            disp.append(sentence2)
    return ", ".join(disp)

#To test the code:

n = 5       
phrases(n)


###Python Challenge #4: The Tribonacci Sequence Challenge
###The "Tribonacci sequence" challenge is a twist on the famous Fibonacci sequence, where each number is the sum of the preceding three numbers.
###The challenge: Write a function that returns the nth number in the Tribonacci sequence.

disp = []

def seq(n, a, b, c):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    # Initialise the first three terms of the Tribonacci sequence
    for i in range(3, n+1):
        next_term = a + b + c
        a, b, c = b, c, next_term
    return c #only return the nth number in the Tribonacci sequence   

#To test the code:
        
seq(5, 0, 1, 1)


###Python Challenge #5: Hide a Credit Card Number
###The challenge: Write a function that takes a credit card number and transforms it into a string where all digits except the last four are replaced with asterisks.

def credit_card(a):

    b = str(a)

    first_char = b[:len(b)-4]
    last_char = b[-4:]
    print('Last character : ', last_char)
    print('first character : ', first_char)

    replacement = '####'

    x = first_char + replacement
    
    return x

#To test the code:
    
a = int(12345678987654321) # Enter any number
credit_card(a)

###Python Challenge #6: SpongeCase
###The challenge: Write a function that converts the given string into spongcase.

a = 'SpongeCase'

def texting_style(a):
    l = len(a)
    word = []
    i = 0
    while i < l:
        cap1 = a[i].upper()
        i = i + 1
        word.append(cap1)
        cap2 = a[i].lower()
        i = i + 1
        word.append(cap2)
    print(''.join(word))

#To test the code:
    
texting_style(a)


###Python Challenge #7: Caesar Encryption
###The challenge: Create a function that has two parameters – a string to be encoded and an integer representing the number of positions each letter should be shifted.
     
def caesar_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

#To test the code:
    
text = "HelloWorld"
shift = 1

caesar_encryption(text, shift)


###Python Challenge #8: Is the Product Divisible by the Sum?
###The challenge: Create a function that takes a list of integers and returns whether the product of those integers is divisible by their sum or not.

#if there are two numbers

def prod_div_by_sum(x, y):
    
    z1 = x * y
    z2 = x + y
    
    if z1 % z2 == 0:
        return True
    else:
        return False
    
#To test the code:
    
prod_div_by_sum(4, 4)
#OR
prod_div_by_sum(4, 7)

#if there is a list of numbers

list_int = []
    
def prod_div_by_sum(list_int):
    
    if np.prod(list_int) % np.sum(list_int) == 0:
        return True
    else:
        return False
    
#To test the code:
    
prod_div_by_sum([1, 2, 3])
#OR
prod_div_by_sum([2, 3, 4])




