#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Random walk simulator for stock prices and pricing european call options
"""
import numpy as np

# Parameters
sigma = 0.4   # Volatility
interest = 0.05  # Risk-free interest rate
stckinit = 100  # Initial stock price
dt = 1/252  # Small time step (1 trading day)
n_steps = 252  # Number of trading days in a year

# Time domain
domain = np.linspace(0, n_steps, n_steps)

"""
the rdwalk is a function that takes x=stockprice, y=interest rate, and z=sigma to return a new random stock price
dt= the number of steps we take, 242 is the number of trading days in a year
"""
def rdwalk(x,y,z,dt):
    result=x+(x*y*dt)+(x*z*np.sqrt(dt)*np.random.normal(0,1))
    return result

# Generate stock prices
stockprices = np.zeros(n_steps)
stockprices[0] = stckinit  # Set initial price

for k in range(1, n_steps):
    stockprices[k] = rdwalk(stockprices[k-1], interest, sigma, dt)


"""
Now we can price the calls
"""
#strike price
strike=120

#how many times we'll repeat our random walk
repeat=1000

payarray=np.zeros(repeat)

for j in range(0,repeat):
    for k in range(1, n_steps):
        stockprices[k] = rdwalk(stockprices[k-1], interest, sigma, dt)
    payarray[j]=np.maximum(strike-stockprices[n_steps-1],0)

average=np.mean(payarray)
fairprice=average*np.exp(-sigma)
confidenceint=1.96*np.std(payarray)/np.sqrt(repeat)
print(f"The fair price is {fairprice} dollars, and the 95% confidence interval is plus or minus {confidenceint}.")
