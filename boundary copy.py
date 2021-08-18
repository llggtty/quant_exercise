# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#def base_number():
#    yield 1
#    for i in range(2,10,2):
#        yield i
#    for i in base_number():
#        yield i*10
#        
#
#        
#def boundary(n):
#    for i in base_number():
#        print("i: ", i)
#        if i>n:
#            return i   

#print("boundary 5: ", boundary(5))
#print(boundary(432))
#print(boundary(2048))
#print(boundary(178945))

#i = 0
#j = 1
#while i<100:
#    new = i + j
#    print(new)
#    i = j
#    j = new
    

#def fibonacci():
#    i = 0
#    j = 1
#    yield 0
#    yield 1
#    new = i + j
#    yield new
#    while new >= 1:
#        i = j
#        j = new
#        new = i+ j 
#        yield new
def fibonacci():
    i = 0
    j = 1
    while True:
        yield i
        i,j=j,i+j
        
    
for n in fibonacci():
    print(n)
    if n>100:
        break