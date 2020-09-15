# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:35:07 2020

@author: Adhiraj
"""


for i in range(1,101):
    if i % 3 == 0 and i % 15 != 0:
        print ("fizz")
    elif i % 5 == 0 and i % 15 != 0:
        print ("buzz")
    elif i % 15 == 0:
        print ("fizzbuzz")
    else:
        print (i)
        