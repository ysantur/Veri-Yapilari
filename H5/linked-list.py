#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 22:57:55 2018

@author: sntr
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 


node1 = Node(12) 
node2 = Node(99) 
node3 = Node(37) 
node1.next = node2 # 12->99
node2.next = node3 # 99->37

