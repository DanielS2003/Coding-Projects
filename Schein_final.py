#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daniel B. Schein Jr
Final Project
Final_Project.py
Comments: Just writing down the Fnet equation and variables
Resistive force R=((D*p*A)/2)*v**2
Where D= drag coefficient
p= density of air
A= frontal area
v= velocity
So then the sum of the vertical forces = mg-((D*p*A)/2)*v**2
"""

import numpy as np
import matplotlib.pyplot as plt

dia=.2159 #the diameter of a bowling ball in meters according to google
m=7.3 #mass of the bowling ball in kilograms
g=9.81 #acceleration due to gravity
v=0 #we're assuming that the initial velocity is 0 m/s
D= 0.5 #the drag constant we're supposed to be using
p=1.225 #density of air near sea level in kg/m**3 according to google
y=0 #this is the initial position
t=0 #initial time
#y-final is 440 meters, assuming that down is in the positive y direction
A=(np.pi*(dia/2)**2) #this is the frontal Area, assuming that only half the bowling ball is exposed to the air flow

sub=(D*p*A)/(2*m) #substitution for the value this equates to because it pops it multiple times in the code


N=40
dt=.25 #the delta t we use

#this is past Daniel speaking, please fix the N, dt, and time array so that you can alter dt such that you get the percent diff below 1% later on, I'll write the report.
#This is future daniel, no, I'd rather not.
time=np.linspace(t,9.5,N) #the time range of values now goes from 0 to 9.5 seconds(the time it takes to hit the ground neglecting air resistance sampled N times

position=np.array([y]) #the position array that we will be finding the values for as the ball falls
velarray=np.array([v]) #the velocity array, I will use both later on for part 2 and 3
#part 1 is the code below
while t<=9.5: #this will do the loop until the t value is 9.5 seconds, which is how long it would take for the ball to hit the ground neglecting air resistance
    t=t+dt #iterating time by dt
    
    v=v+(g-((sub)*(v**2)))*dt #using simple euler's method for velocity
    
    velarray=np.append(velarray,v) #appending to the velocity array
    
    y=y+v*dt #the approximation for position
    
    #after doing these calcs, we append to the array
    position=np.append(position, y)

#plotting the time and velocity data
plt.plot(time,velarray)
plt.title("Velocity vs Time")
plt.xlabel("Time")
plt.ylabel("Velocity")

#part 2 now
vexarray=(np.sqrt((2*m*g)/(D*p*A)))*np.tanh(np.sqrt((D*p*A*g)/(2*m))*time) 
#exact velocity at a time, given by the equation, vectorized over the time array


#when t=9.5, the time array is at its 38th element, so the velarray at its 38th element will be used in calcing diff
plt.plot(time,vexarray,'r-') #plotting the exact velocity vs time on the same graph as before
vdiff= ((velarray[38]-vexarray[38])/velarray[38])*100 #the percent difference between exact, and euler's method for velocity at t=9.5 seconds

#part 3 now

pexarray=(((2*m)/(D*p*A))*np.log(np.cosh((time*np.sqrt((D*p*A*g)/(2*m))))))
 #exact position at a time

pdiff=((position[38]-pexarray[38])/position[38])*100 #finding the diff between the positions at time=9.5

#this code below creates a second figure for the position data, both the exact and Euler's method data
plt.figure(2)
plt.plot(time, position)
plt.plot(time,pexarray, 'r-')
plt.title("Position vs Time")
plt.xlabel("Time")
plt.ylabel("Position")


#part 4 now
N=100
time=np.linspace(0,10.9,N)

FartArray=(((2*m)/(D*p*A))*np.log(np.cosh((time*np.sqrt((D*p*A*g)/(2*m)))))) 
#This fart array is the exact position array but done more exactly so that I can tell you when the ball hits the ground, if you're wondering where the name comes from, I was orginially naming it fpartarray, for final part array, which was shortened to fartarray
#When examining the array, the value closest to 440 is the 96th element so then the time element is also the 96th and that is the approximate time when the ball hits the ground
