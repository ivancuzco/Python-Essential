# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:17:16 2023

@author: user
"""

acl=int(input("ingrese el numero de ACL: "))
if acl>=1 and acl<=99:
    print("la ACL es estandard")
elif acl>=100 and acl<=199:
    print("la ACL es extendida")
else:
    print("no es un numero de ACL")