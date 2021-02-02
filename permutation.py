#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:50:51 2020

@author: natnem
"""

#def get_permutations(sequence):
#    if len(sequence) <= 1:
#        return [sequence]
#    else:
#        permutations = []
#        first_char = sequence[0]
#        last_chars = sequence[1:]
#        perm_of_seq = get_permutations(last_chars)
#        
#        for seq in perm_of_seq:
#            for ind in range(len(seq)+1):
#                newseq = seq[0:ind] + [first_char] + seq[ind:len(seq)+1]
#                permutations.append(newseq)
#                print(ind,first_char,newseq)
#        return permutations
#    
#example_input = ['a','b','c']
#print(get_permutations(example_input))


def listPermutations(string, chosen):
    if string == "":
        return chosen
    else:
        permutation = []
        for i in range(0,len(string)):
            ch = string[i]
            remaining = string[0:i] + string[i+1:len(string)]
            permuted = listPermutations(remaining, chosen + ch)
            permutation.append(permuted)
        return permutation
            
    
mystring = "12"
chosen = ""
print(listPermutations(mystring , chosen))
