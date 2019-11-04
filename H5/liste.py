# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:03:55 2019

Çift yönlü bağlı liste
"""

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.previousnode = None

    
    def setNextNode(self,node):
        self.nextnode = node
        
    def getNextNode(self):
        return self.nextnode

    def setPreviousNode(self,node):
        self.previousnode = node
        
    def getPreviousNode(self):
        return self.previousnode

    def getNodeValue(self):
        return self.value


x=Node("10")
y=Node("20")
z=Node("30")

x.nextnode=y
y.nextnode=z
y.previousnode=x
z.previousnode=y

print(z.getPreviousNode().getNodeValue())