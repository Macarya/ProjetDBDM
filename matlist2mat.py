# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:33:24 2017

@author: Xavier
"""

def mtxl2m(M):
    return [[-1 for l in t if not len(l) else sum(l)/len(l)] for t in M]