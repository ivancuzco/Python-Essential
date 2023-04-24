# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:21:41 2023

@author: user
"""
while True:
    x=input("enter a number to coun to: ")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y+=1
        if y>x:
            break
    break
    
