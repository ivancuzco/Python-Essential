# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:22:55 2023

@author: ENTERPRISE
"""

def saludos03(lista):
    for item in lista:
        print("hola,", item)
    print("")
saludos03(["ana","luis","carmen"])
saludos03(["ana","luis"])

def crealista(n):
    lista=[]
    for item in range(1,n+1,1):
        lista.append(item)
    return lista
print(crealista(10))
