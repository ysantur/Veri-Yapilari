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
        #print(list)
        

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


def quicksort(list):
    boyut = len(list)
    if(boyut <= 1):
        return list
    else:
        pivot = list[0]
        buyuk = [ i for i in list[1:] if i > pivot ]
        kucuk = [ i for i in list[1:] if i <= pivot ]
        return quicksort(kucuk) + [pivot] + quicksort(buyuk)

#Merge sort rekürsif
def merge(left,right):
    merged = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        merged += right
    else:
        merged += left
    return merged


def mergesort(list):
    if len(list) <= 1:
        return list
    else:
        middle = len(list)//2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])
        return merge(left,right)
#Merge sort rekürsif

def merge_sort(list):
    start = []
    end = []
    while len(list) > 1:
        a = min(list)
        b = max(list)
        start.append(a)
        end.append(b)
        list.remove(a)
        list.remove(b)
    if list: start.append(list[0])
    end.reverse()
    return (start + end)



def radixsort(list):
    n = len(list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in list:
            least_digit = value % modulus
            least_digit //= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == n:
            return new_list[0]

        list = []
        rd_list_append = list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)


def countingsort(list):
    max_val=max(list)
    m = max_val + 1
    count = [0] * m                
    for a in list:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            list[i] = a
            i += 1
    return list


list = [19,2,31,45,6,11,121,27]
#print(list)
#bubblesort(list)
#insertionsort(list)
#selectionsort(list)
#shellsort(list)
#quicksort(list)
print(countingsort(list))