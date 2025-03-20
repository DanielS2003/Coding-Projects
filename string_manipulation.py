#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
string manipulation program for python practice
"""

word=input("Enter your word(s): ")
lowword=word.lower()
lowword=lowword.replace(" ","")

reverse=lowword[::-1]    

if lowword==reverse:
    print("Your word is a palindrome")

else:
    print("Your word is not a palindrome")
    
vowels= ['a','e','i','o','u']

vowelcount=0

for character in lowword:
    for vowel in vowels:
        if character==vowel:
            vowelcount+=1

print(f"The number of vowels in your word is: {vowelcount}")