# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:15:59 2023

@author: user
"""

contar=input("ingrese el numero al que se debe contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>contar:
        break
    