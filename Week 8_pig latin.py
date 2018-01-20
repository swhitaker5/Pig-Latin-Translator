# -*- coding: utf-8 -*-
"""
By: Shatavia Whitaker (SID: 1616798)
Created:  11.29.2017
Modified: 11.30.2017

Write a program to convert text into Pig Latin. This inolves two steps: move any 
consonant (or cluster) that appears at the start of the word to the end, then append ay.
"""



import re                                                                                      #Import for regular expressions

mystring = input("Enter anything you would like translated to Pig Latin: \n").lower()          #String input. Converts to lowercase
split_string = mystring.split()                                                                #splits string by word
pl_trans = []

vowel_list = ('a','e','i','o','u','y')                                                         #tuple of vowels
punc = ('.',',',':',';','!','?'"'",'"')                                                        #tuple for puncuations

for word in split_string:
    c = re.search(r"(?P<cluster>[^aeiouy]+)?(?P<remainder>\w+)(?P<punc>([.,!?:;]?))", word)    #re to seperate const and body of word + any puncation
    if word.startswith(vowel_list):                                                            #combination for words starting w/ vowel
        pig_latin = (c.group('remainder') + 'ay') 
    else:                                                                                      #combination for words stating w/ consonants
        pig_latin = (c.group('remainder') + c.group('cluster') + 'ay')    
    if word.endswith(punc):                                                                    #If there are any puncuations after the word
        pig_latin = pig_latin + c.group('punc')
    pl_trans.append(pig_latin)                                                                 #adds newly created word to a list
       
print(' '.join(pl_trans))                                                                      #takes the pl_trans list and makes it a string
    
        
