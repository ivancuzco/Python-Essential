# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:45:00 2023

@author: user
"""

try:
    x=int(input("enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You can not devide by zero, sorry.")
except ValueError:
    print("you must enter a integer value.")
except:
    print("Oh dear, something went wrong...")
print("the end")