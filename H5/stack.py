#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:04:12 2018

@author: sntr
"""

class Stack(object):

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit


    def push(self, data):
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('Stack boş')

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print('Stack boş')

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


x = Stack()
x.push(5)
print(x.pop())
x.push(7)
print(x.size())
print(x.is_empty())
print(x.top())
print(x.size())