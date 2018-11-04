#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 23:17:31 2018

@author: sntr
"""

class Queue():
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front=0

    #Kuyruğun sonuna eleman ekler
    def insert(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    #Kuyruğun başındaki elemanı çeker.
    def remove(self):
        if self.length>0:
            item=self.entries[0]
            self.length = self.length - 1
            del self.entries[0]
            return item
        else:
            print("Kuyruk boş")

    #Kuyruğun başındanki elemanı çeker, silmeden.
    def front(self):
        return self.entries[0]

    #Kuyruktaki eleman sayısı
    def size(self):
        return self.length
    
    #Kuyruğu yazdır
    def show(self):
        print(self.entries)


x=Queue()
x.insert(1)
x.insert(2)
x.show()
x.remove()
x.remove()
x.remove()

x.show()