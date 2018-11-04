#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 22:33:44 2018

@author: sntr
"""

x=list()            #Boş liste
x.append(1)         #Sonuna eleman ekle 
x.append(3)
x.append(5)

print(len(x))       #Listenin uzunluğu
 
print(x.index(3))   #Değeri 3 olan elemanın yerini dönder

x.insert(1,2)       #Araya eleman ekle
x.insert(3,4)

print(x[-1])        #En üstteki veriyi seç, silmeden!

x.pop()             #En üstteki veriyi seç, silerek! 

x.sort()            #Sırala
x.reverse()         #Ters sırala


