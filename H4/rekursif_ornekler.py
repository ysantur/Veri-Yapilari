# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:08:45 2018

@author: papatya
"""

def faktoriyel(n):     
	if n==1:         
		return 1     
	else:         
		return n*faktoriyel(n-1)
    
    
def faktoriyel_kisa(n):     
	return 1 if n==1 else  n*faktoriyel(n-1) 
  

print (faktoriyel_kisa(6))