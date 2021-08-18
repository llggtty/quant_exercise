"""
You have a biased coin, but you don’t know exactly how biased it is. 
The probability of it falling heads is any number between 0 and 1. 
You have 1000 USD in your pocket when Gary offers you to play a game – 
you can bet any increment of 1 USD to bet on one side of the coin. 
Afterwards, Gary throws the coin in the air and if it lands on the side you’ve chosen, your bet is doubled. 
If it doesn’t, Gary takes the amount you’ve bet.
Write a program that plays this game to maximize your net worth growth 
(or a logarithm of net worth) in terms of times the coin was flipped.

"""


import numpy as np
        
# the growth could depend on the ratio of testing and the bet size
def simulation(r_est,r_bet,p):
    n_est = np.max([int(n_total * r_est), 1])
    flips = np.random.binomial(1,p,n_total)
    
    p_est = flips[0:n_est].sum()/n_est
    if p_est < 0.5:
        worth = fund  + (flips[0:n_est].sum() * 2 - n_est)
    else:    
        worth = fund
        for i in range(n_est, n_total):
            x = worth * r_bet
            worth = worth + flips[i]*x*2 - x    
    return worth

def process(n_total,p):
    payoff_max = simulation(0.1, 0.1,p)
    for r_est in np.linspace(0.1, 0.9, 9):
        for r_bet in np.linspace(0.1, 0.9, 9):
            payoff = simulation(r_est,r_bet,p)
            if payoff > payoff_max:
                payoff_max = payoff
                print("improvement found. estimating ratio: ",r_est,"betting ratio: ",r_bet )
            
p = 0.8
fund = 1000 
n_total = 100

for p in np.linspace(0.5,0.9,5):
    print("in the case of p = ",p)
    process(n_total,p)
    
# from the results, I will fix the estimate ratio at 0.1, seem to be robust. 
# so I first estimate p, and process simulation. use the r_bet it thinks it's best
def finding_bet_size(p_est):
    payoff_max = simulation(0.1, 0.1,p_est)
    # to find r_bet
    r_bet_max = 0.1
    for r_bet in np.linspace(0.1, 0.9, 9):
        payoff = simulation(0.1,r_bet,p_est)
        if payoff > payoff_max:
            payoff_max = payoff
            r_bet_max = r_bet
            print("improvement found. betting ratio: ",r_bet_max, "worth: ", worth ) 
    return r_bet_max

def robot(n_total):
    n_est = np.max([int(n_total * 0.1), 1])
    flips = np.random.binomial(1,p,n_total)
    
    p_est = flips[0:n_est].sum()/n_est
    if p_est < 0.5:
        worth = fund  + (flips[0:n_est].sum() * 2 - n_est)
    else:      
        r_bet = finding_bet_size(p_est)
        worth = fund
        for i in range(n_est, n_total):
            x = worth * r_bet
            worth = worth + flips[i]*x*2 - x   
        print("betting ratio: ",r_bet, "worth: ", worth )


robot(n_total)
"""
p = 0.8
fund = 1000
# Say I want good return in n_total times
# I bet on 1, if p > 0.5, I should flip, if p<=0.5, I stop playing
# I take first 10% n_est times of flips to estimate p.
n_total = 100
n_est = np.max([int(n_total * 0.1), 1])
# all the flips I need
flips = np.random.binomial(1,p,n_total)

p_est = flips[0:n_est].sum()/n_est
if p_est < 0.5:
    worth = fund  + (flips[0:n_est].sum() * 2 - n_est)
else:
    # When p > 0.5, I want to find the best betting size
    # say always bet half of the net worth
    worth = fund
    for i in range(n_est, n_total):
        x = worth * 0.5
        worth = worth + flips[i]*x*2 - x
        
"""
