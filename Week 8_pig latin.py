# -*- coding: utf-8 -*-
"""
By: Shatavia Whitaker (SID: 1616798)
Created:  11.29.2017
Modified: 11.30.2017

Write a program to convert text into Pig Latin. This inolves two steps: move any 
consonant (or cluster) that appears at the start of the word to the end, then append ay.
"""

import re

mystring = input("Enter anything you would like translated to Pig Latin: \n").lower()
split_string = mystring.split()
pl_trans = []

vowel_list = ('a','e','i','o','u','y')
punc = ('.',',',':',';','!','?'"'",'"')          
i = 0 

for word in split_string:       
    if word.startswith(vowel_list):
        vwl = word + 'ay'
        pl_trans.append(vwl)
    else:
        c = re.search(r"(?P<cluster>(^|\s)[^aeiou]+)(?P<remainder>\w+)", word)
        pig_latin = (c.group('remainder') + c.group('cluster') + 'ay')
        pl_trans.append(pig_latin)
       
print(' '.join(pl_trans))
    
        
