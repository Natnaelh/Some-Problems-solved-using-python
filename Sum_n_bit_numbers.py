#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:41:43 2020

@author: natnem
"""

A = [1,1,1,1]
B = [1,1,1,1]

def SumBits(A, B):
    C = [0 for x in range(len(A)+1)]
    c = 0
    for i in range((len(A)-1),-1,-1):
        ans = A[i] + B[i] + c
        if ans == 2:
            ans = 0
            c = 1 
        elif ans == 3:
            ans = 1
            c = 1
        C[i+1] += ans
    C[0] = c
    return  C[::1]
print(SumBits(A,B))
