#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A loan repayment calculator
"""

A=float(input("What amount do intend to take out?: "))

t=float(input("In how many years do you plan to pay the loan off?: "))

r=float(input("What is the annual interest rate on the loan?(in decimal form): "))

n=float(input("How many yearly payments will you make?: "))

payment=(A*(r/n)) / (1-(1+r/n)**(-n*t))
totrpyd=payment*n*t

print(f"Your payments will be: {payment}")
print(f"The total amount repayed is: {totrpyd}")
