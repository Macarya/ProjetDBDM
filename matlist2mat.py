# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:33:24 2017

@author: Xavier
"""

M = [[[1,2],[],[1,5,6,7]],[[1,19,0.122],[],[1,5,6,7]],[[1,2],[],[1,5,6,7]]]

def mtxl2m(M):
    return [[-1 if not len(l) else sum(l)/len(l) for l in t] for t in M]

