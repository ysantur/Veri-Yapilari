# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:17:50 2019
Çift yönlü bağlı lsite eleman ekleme ve çıkarma
"""
class Node(object):
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
class Liste(object):

    cnt=0
    head=None
    tail=None
        
    def add(self,data):
        new_node=Node(data,None,None)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            new_node.prev=self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        Liste.cnt+=1


    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                if current_node.prev is  None:
                    self.head = current_node.next
                    current_node.next.prev = None

                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
 
            current_node = current_node.next
        Liste.cnt-=1
            
    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def length(self):
        return Liste.cnt
    

liste=Liste()

liste.add("3")


liste.print()

#print(liste.length())

