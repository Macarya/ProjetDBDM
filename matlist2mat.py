# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:33:24 2017

@author: Xavier
"""

from parsing import parse,aff

    
def moyenne(l):
    if (not len(l)):
        return (-1,0)
    moy = sum(l)/len(l)
    a = 0;
    for x in l:
        a+=(x-moy)**2
    return [moy,a/len(l)]

def moyenne_sans_quartil(l,q=4):
    n = len(l)
    if(not n):
        return -1,0
    l_tempo = sorted(l)
    return moyenne(l_tempo[(n//q):min(n,(q-1)*((n+q)//q))])
    
def mtxl2m(M,f=moyenne):
    return [[f(l) for l in t] for t in M]

def ll2m(L,f=moyenne):
    return [f(l) for l in L]


def dist2m_moya(M1,M2):
    a = 0;
    k = 0;
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if (M1[i][j][0]>0 and M2[i][j][0]>0):
                a+=abs(M1[i][j][0]-M2[i][j][0])
                k+=1
    if k > 0:
        return a/k
    return -1

def dist2m_moyg(M1,M2):
    a = 0;
    k = 0;
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if (M1[i][j][0]>0 and M2[i][j][0]>0):
                if (M1[i][j][0]>M2[i][j][0]):
                    a+=M1[i][j][0]/M2[i][j][0]
                else :
                    a+=M2[i][j][0]/M1[i][j][0]
                k+=1
    if k > 0:
        return a/k
    return -1


def dist2l_moya(L1,L2):
    a = 0;
    k = 0;
    for i in range(len(L1)):
        if (L1[i][0]>0 and L2[i][0]>0):
            a+=abs(L1[i][0]-L2[i][0])
            k+=1
    if k > 0:
        return a/k
    return -1

def dist2l_moyg(L1,L2):
    a = 0;
    k = 0;
    for i in range(len(L1)):
        if (L1[i][0]>0 and L2[i][0]>0):
            if (L1[i][0]>L2[i][0]):
                a+=L1[i][0]/L2[i][0]
            else :
                a+=L2[i][0]/L1[i][0]
            k+=1
    if k > 0:
        return a/k
    return -1

Lxa,Mxa = parse('xavier_dicté.txt')
Lra,Mra = parse('redouane_dicté.txt')
Lxt,Mxt = parse('xavier_test.txt')
Lrt,Mrt = parse('redouane_test.txt')
Lxl,Mxl = parse('xavier_lorem_ipsum.txt')
Lxc,Mxc = parse('xavier_copie_daudet_derniere_classe.txt')

Mxa1 = mtxl2m(Mxa,moyenne_sans_quartil)
Mra1 = mtxl2m(Mra,moyenne_sans_quartil)
Mxt1 = mtxl2m(Mxt,moyenne_sans_quartil)
Mrt1 = mtxl2m(Mrt,moyenne_sans_quartil)
Mxl1 = mtxl2m(Mxl,moyenne_sans_quartil)
Mxc1 = mtxl2m(Mxc,moyenne_sans_quartil)

Lxa1 = ll2m(Lxa,moyenne_sans_quartil)
Lra1 = ll2m(Lra,moyenne_sans_quartil)
Lxt1 = ll2m(Lxt,moyenne_sans_quartil)
Lrt1 = ll2m(Lrt,moyenne_sans_quartil)
Lxl1 = ll2m(Lxl,moyenne_sans_quartil)
Lxc1 = ll2m(Lxc,moyenne_sans_quartil)


#print(dist2m_moyg(Mxa1,Mra1))
print("juste")
print(dist2m_moyg(Mxa1,Mxt1))
print("faux")
print(dist2m_moyg(Mxa1,Mrt1))
print(dist2m_moyg(Mra1,Mxt1))
#print(dist2m_moyg(Mra1,Mrt1))
#print(dist2m_moyg(Mxa1,Mxl1))
#print(dist2m_moyg(Mra1,Mxl1))
#print(dist2m_moyg(Mxt1,Mxl1))
#print(dist2m_moyg(Mrt1,Mxl1))
print("juste")
print(dist2m_moyg(Mxa1,Mxc1))
print(dist2m_moyg(Mxt1,Mxc1))
print(dist2m_moyg(Mxl1,Mxc1))
print("faux")
print(dist2m_moyg(Mxc1,Mrt1))
print(dist2m_moyg(Mxc1,Mra1))

print("\n ari \n")

#print(dist2m_moya(Mxa1,Mra1))
print("juste")
print(dist2m_moya(Mxa1,Mxt1))
print("faux")
print(dist2m_moya(Mxa1,Mrt1))
print(dist2m_moya(Mra1,Mxt1))
#print(dist2m_moya(Mra1,Mrt1))
#print(dist2m_moya(Mxa1,Mxl1))
#print(dist2m_moya(Mra1,Mxl1))
#print(dist2m_moya(Mxt1,Mxl1))
#print(dist2m_moya(Mrt1,Mxl1))
print("juste")
print(dist2m_moya(Mxa1,Mxc1))
print(dist2m_moya(Mxt1,Mxc1))
print(dist2m_moya(Mxl1,Mxc1))
print("faux")
print(dist2m_moya(Mxc1,Mrt1))
print(dist2m_moya(Mxc1,Mra1))

print("\n touche \n")

#print(dist2l_moyg(Lxa1,Lra1))
print("juste")
print(dist2l_moyg(Lxa1,Lxt1))
print("faux")
print(dist2l_moyg(Lxa1,Lrt1))
print(dist2l_moyg(Lra1,Lxt1))
#print(dist2l_moyg(Lra1,Lrt1))
#print(dist2l_moyg(Lxa1,Lxl1))
#print(dist2l_moyg(Lra1,Lxl1))
#print(dist2l_moyg(Lxt1,Lxl1))
#print(dist2l_moyg(Lrt1,Lxl1))
print("juste")
print(dist2l_moyg(Lxa1,Lxc1))
print(dist2l_moyg(Lxt1,Lxc1))
print(dist2l_moyg(Lxl1,Lxc1))
print("faux")
print(dist2l_moyg(Lxc1,Lrt1))
print(dist2l_moyg(Lxc1,Lra1))

print("\n ari \n")

#print(dist2l_moya(Lxa1,Lra1))
print("juste")
print(dist2l_moya(Lxa1,Lxt1))
print("faux")
print(dist2l_moya(Lxa1,Lrt1))
print(dist2l_moya(Lra1,Lxt1))
#print(dist2l_moya(Lra1,Lrt1))
#print(dist2l_moya(Lxa1,Lxl1))
#print(dist2l_moya(Lra1,Lxl1))
#print(dist2l_moya(Lxt1,Lxl1))
#print(dist2l_moya(Lrt1,Lxl1))
print("juste")
print(dist2l_moya(Lxa1,Lxc1))
print(dist2l_moya(Lxt1,Lxc1))
print(dist2l_moya(Lxl1,Lxc1))
print("faux")
print(dist2l_moya(Lxc1,Lrt1))
print(dist2l_moya(Lxc1,Lra1))
