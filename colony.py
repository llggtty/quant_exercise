#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:33:30 2018

@author: annhuang


Bacterial colony
A bacterial colony consists of individual bacteria. One of the following happens with each bacterium each second:
 The bacterium dies.
 The bacterium remains without a change.
 The bacterium splits in two bacteria.
 The bacterium splits in three bacteria.
Each of the above happens with equal probability 25%. 
Your task is to estimate probability that the bacterial colony, which initially consists of one bacterium, 
will never die.
"""
# for one generation
import numpy as np
class One():
    def __init__(self, number):
        self.count = number
    def remain(self,n1):
        self.n1 = n1
    def split_2(self, n2):
        self.n2 = 2*n2
    def split_3(self, n3):
        self.n3 = 3*n3
    def simulate(self):
        state = np.random.uniform(0,1,self.count)*4
        state = [int(np.floor(x)) for x in state]
        self.remain(state.count(1))
        self.split_2(state.count(2))
        self.split_3(state.count(3))
        self.count = self.n1 +self.n2 + self.n3
               

bacterium = One(100)
bacterium.count 
bacterium.simulate()
bacterium.count  
# let's say if the count is big enough (500), then the colony never die
# or if the number of loop is big enough (500)
def run_once(n_loop, numbers):
    num_unstop = numbers[0]
    num_exceed_loop = numbers[1]
    g = One(1) 
    
    for i in range(1,n_loop):
        g = One(g.count)
        g.simulate()
        
        if g.count==0:
            break        
        if g.count>500:
            num_unstop = num_unstop +1 
            break
        if i == n_loop -1:
            num_exceed_loop= num_exceed_loop+1
    return [num_unstop, num_exceed_loop]
        
    

def simulate(n_sim,n_loop):

    numbers = [0,0]
    for i in range(0,n_sim):
        numbers = run_once(n_loop, numbers)
    prob = (numbers[0]+numbers[1])/n_sim
    return prob

prob = simulate(1000,500)
    
   # prob = 0.55 
        

