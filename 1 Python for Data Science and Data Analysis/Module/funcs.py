# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:40:02 2021

@author: xwyzworm
"""


def checkIfNumeric(*args : any):
    ans = []
    for i in args:
        if not(isinstance([int,float], i)):
            ans.append(False)
        else:
            ans.append(True)
            
        return ans

def returnTheOdds(*args :any):
    ans :any = list()
    for i in (args):
        if i % 2 == 0:
            ans.append(i)
    return ans

def sumIt(*args : any):
    ans : int = 0
    for i in args:
        ans += i
    return ans
