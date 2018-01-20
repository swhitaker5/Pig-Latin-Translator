# -*- coding: utf-8 -*-
"""
By: Shatavia Whitaker (SID: 1616798)
Created:  11.29.2017
Modified: 11.30.2017

Write a program to convert text into Pig Latin. This inolves two steps: move any 
consonant (or cluster) that appears at the start of the word to the end, then append ay.
"""



import re                                                                                   #Import for regular expressions

mystring = input("Enter anything you would like translated to Pig Latin: \n").lower()       #String input. Converts to lowercase
split_string = mystring.split()                                                             #splits string by word
pl_trans = []

vowel_list = ('a','e','i','o','u','y')                                                      #tuple of vowels
punc = ('.',',',':',';','!','?'"'",'"')          
i = 0 

for word in split_string:       
        if word.startswith(vowel_list):
        v = re.search(r"(?P<the_word>[\w]+)(?P<punc>([.,!?:;]?))", word)
        vwl = v.group('the_word') + 'ay'
        if word.endswith(punc):
            vwl = vwl + v.group('punc')
            pl_trans.append(vwl)
        else:
            c = re.search(r"(?P<cluster>[^aeiou]+)(?P<remainder>\w+)(?P<punc>([.,!?:;]?))", word)
            pig_latin = (c.group('remainder') + c.group('cluster') + 'ay')
            if word.endswith(punc):
                pig_latin = pig_latin + c.group('punc')
                pl_trans.append(pig_latin)
       
print(' '.join(pl_trans))
    
        
