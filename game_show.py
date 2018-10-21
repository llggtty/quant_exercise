#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:38:43 2018

@author: annhuang

Game show
You participate in a game show. The game consists of n rounds. 
During each round, the game show host proposes you a prize of a known value (in USD). You have two choices:
 You can take the prize and end the game.
 You can reject the prize and continue the game. If you reject the prize, which was proposed to
you during the last round, you will not get any price (you can think about it as you get a prize of
value 0 USD).
It is known that the values of proposed prizes are independent and identically distributed random variables. 
It is also known that the values of proposed prizes have binominal distribution with parameters 40 and 0.7.
Here is an example of a possible game show scenario. Bob participates in a game show which consist from 3 rounds 
(n=3).
 During the first round Bob is proposed a price of value 15 USD. Bob rejects the price. 
Therefore the second round starts.
 During the second round Bob is proposed a price of value 20 USD. Bob accepts the price. 
Since Bob accepted the price, the game ends, and there is no third round.
Your task is to write a program, which for a given number of rounds n outputs optimal game strategy. 
The optimal game strategy maximizes expected value of the received prize. 
The optimal strategy can be described as an array A of prize values. 
If the value of the prize proposed on the round i is grater or equal then A[i] than you take the prize, 
otherwise you continue the game.
"""

import numpy as np
n_sim = 5000
y = np.random.binomial(40,0.7,n_sim)
# bin distribution
def bino_p(x,y):
    return sum(y>x)/n_sim

def bino_e(x,y):
    if len(y[y>x])>0:
        return sum(y[y>x])/len(y[y>x])
    else:
        return 0

#E(x) = 28
# at the last run, it's optimal to take anything, so A[-1] =0
# the previous run, if offer is x, which is smaller than Ex, I will turn down. so A[-2] = Ex
# the n-2 run, A[-3] = p(x<=A[-2])*A[-2] +p(x>A[-2])*E(x|x>A[-2])

def optimal(rounds):
    ex = 40*0.7
    y = np.random.binomial(40,0.7,10000)
    amounts = np.repeat(0.0, rounds-1)
    amounts[-1] = 0
    amounts[-2] = ex
    for i in range(3, rounds):
        previous_accept = amounts[-i+1]
        p=bino_p(previous_accept,y)
        current_accept = p* bino_e(previous_accept,y) + (1 - p)*previous_accept
        amounts[-i] = current_accept        
    return amounts

print(optimal(10))