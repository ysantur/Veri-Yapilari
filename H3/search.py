# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:33:48 2018

@author: Yunus Santur , ysantur@gmail.com
"""


def lineersearch(list, aranan):
    for i in range(0, len(list)):
        if list[i]==aranan:
            return (i,list[i])
    else:
        return False
    

def simplebinarysearch(list,aranan):
        indis=len(list)//2
        if aranan==list[indis]:
            return (list[indis])
        elif aranan>list[indis]:
            list=list[indis:]
        else:
            list=list[:indis]

        return simplebinarysearch(list,aranan)
    


list = range(100)
print(simplebinarysearch(list, 10))
