# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:33:24 2017

@author: Xavier
"""

M = [[[1,2],[],[1,5,6,7]],[[1,19,0.122],[],[1,5,6,7]],[[1,2],[],[1,5,6,7]]]

def mtxl2m(M):
    return [[-1 if not len(l) else sum(l)/len(l) for l in t] for t in M]

def dist2m(M1,M2):
    a = 0;
    k = 0;
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if (M1[i][j]>0 and M2[i][j]>0):
                a+=abs(M1[i][j]-M2[i][j])
                k+=1
    if k > 0:
        return a/k
    return -1