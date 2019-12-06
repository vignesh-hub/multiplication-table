# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:28:55 2019

@author:vignesh
"""
#for example i am taking 10
#own design actually we need to give 11 for c to print up to length 10
#to solve that i give c=c+1,so user can give 10 itself
#normal person can use this code.....
print("multiplication table")
a=input("which number table you needed: ")
b=int(a)
n=input("up to how much u need the table tell us the lenght :")
c=int(n)
c=c+1
for i in range (c):
    print(i,"x",b,"=",i*b)
