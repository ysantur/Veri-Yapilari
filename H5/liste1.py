# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:05:36 2019

Çift yönlü bağlı liste
eleman sayısı ve ishead, istail
"""

class Node(object):
    length=0
    def __init__(self,value, head=False, tail=False):
        self.value = value
        self.nextnode = None
        self.previousnode = None
        self.head = head
        self.tail=tail
        Node.length+=1
    
    def setNextNode(self,node):
        self.nextnode = node
        
    def getNextNode(self):
        return self.nextnode

    def setPreviousNode(self,node):
        self.previousnode = node
        
    def getPreviousNode(self):
        return self.previousnode

    def ishead(self):
        return True if self.head else False

    def istail(self):
        return True if self.tail else False
    
    def getNodeValue(self):
        return self.value
    

x=Node("10",head=True)
y=Node("20")
z=Node("30",tail=True)

x.nextnode=y
y.nextnode=z
y.previousnode=x
z.previousnode=y

print(z.getPreviousNode().getNodeValue())
print(x.ishead())
print(z.istail())
print(Node.length)