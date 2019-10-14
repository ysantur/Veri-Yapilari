# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:33:48 2018

@author: Yunus Santur , ysantur@gmail.com
"""


def simplelineersearch(list, aranan):
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
    

def simplejumpsearch(list,aranan):
  step=int(len(list)**0.5)

  while(True):
    if list[step]==aranan:
      return list[step]

    elif list[step]>aranan: 
      for i in range(step-1,-1,-1):
        if list[i]==aranan:
          return list[i]
          break

    elif list[step]<aranan:
      if 2*step>=len(list):
        step=len(list)-1
      else:
        step+=step
    else:
      return -1

list = range(100)
print(simplebinarysearch(list, 10))
