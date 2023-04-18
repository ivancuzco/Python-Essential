# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:27:33 2023

@author: user
"""
#en el rango el primer numero es el inicio del rango, el dos final del rango
#y el tercer numero el incremento o decremento
texto="CEC EPN cursos de python ES"
for item in range(1,10+1,1):
    print(item)
print("")
for i in texto:
    print(i,end="")
    #end="" ayuda a colocar de forma horizontal el texto que sale del for
    
o=[]
lista=["a", "b","c","d"]
for x in texto:
    if "o" in x:
        o.append(x)
    print(x,end="")
   
print("")
for elemento in lista:
    print(elemento,end="  ")
    

    