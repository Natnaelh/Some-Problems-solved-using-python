#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:07:48 2020

@author: natnem
"""

def StringMatching(S,t):
    dic = {}
    for i in range(len(t)-len(S)+1):
        s = t[i:i+len(S)]
        if s == S:
            dic[i] = s
             
    return dic

t = "abebe beso bela keza bewla beso belto tetito hedo eroto"
S = "beso"
print(StringMatching(S,t))