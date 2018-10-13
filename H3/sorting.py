# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:33:48 2018

@author: Yunus Santur , ysantur@gmail.com
"""

def bubblesort(list):
   for i in range(0,len(list)):
       for j in range(0,len(list)-i-1):
           if list[j]>list[j+1]:
               temp = list[j]
               list[j] = list[j+1]
               list[j+1] = temp

def insertionsort(list):
    for i in range(1, len(list)):
        while i > 0 and list[i - 1] > list[i]:
            list[i], list[i - 1] = list[i - 1], list[i]
            i -= 1
        print(list)

            

def selectionsort(list):
    for i in range(len(list)):
        minimum = i
        for j in range( i+1, len(list)):
            if list[minimum] > list[j]:
                minimum = j
        list[i], list[minimum] = list[minimum], list[i]
        print(list)
        

def shellsort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j = j-gap
            list[j] = temp
            print(gap," ",list)
        gap = gap//2       



list = [19,2,31,45,6,11,121,27]
#print(list)
#bubblesort(list)
#insertionsort(list)
#selectionsort(list)
shellsort(list)

print(list)