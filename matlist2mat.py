# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:33:24 2017

@author: Xavier
"""

def aff(res):
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j]!=[]:
                print(i,j)


def parse(NomFichier='out.txt'):
    with open(NomFichier,'r') as fichier:
        texte=fichier.read()
        
    texte=texte.split(',')[:-1]
    Resultat=[]
    for j in range(248):
        Resultat.append([ [] for i in range(248)])
    Duree=[ [] for i in range(248)]
    
    pkey,ptime=int(texte[0]),float(texte[2])
    Duree[pkey].append(ptime)
    for n in range(3,len(texte),3):
        key,time=int(texte[n]),float(texte[n+2])
        if texte[n+1]=='+':
            Duree[key].append(-time)
            Resultat[pkey][key].append(time-ptime)
            pkey,ptime=key,time
        else:
            Duree[key][-1]+=time
    return(Duree,Resultat)
    
def moyenne(l):
    if (not len(l)):
        return -1
    return sum(l)/len(l)

def moyenne_sans_quartil(l,q=4):
    n = len(l)
    if(not n):
        return -1
    l_tempo = sorted(l)
    return moyenne(l_tempo[(n//q):min(n,(q-1)*((n+q)//q))])
    
def mtxl2m(M,f=moyenne):
    return [[f(l) for l in t] for t in M]

def dist2m_moya(M1,M2):
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

def dist2m_moyg(M1,M2):
    a = 0;
    k = 0;
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if (M1[i][j]>0 and M2[i][j]>0):
                if (M1[i][j]<M2[i][j]):
                    a+=M1[i][j]/M2[i][j]
                else :
                    a+=M2[i][j]/M1[i][j]
                k+=1
    if k > 0:
        return a/k
    return -1

_,Mxa = parse('out.txt')
_,Mra = parse('out(1).txt')
_,Mxt = parse('out(2).txt')
_,Mrt = parse('out(3).txt')

Mxa1 = mtxl2m(Mxa,moyenne_sans_quartil)
Mra1 = mtxl2m(Mra,moyenne_sans_quartil)
Mxt1 = mtxl2m(Mxt,moyenne_sans_quartil)
Mrt1 = mtxl2m(Mrt,moyenne_sans_quartil)

print(dist2m_moyg(Mxa1,Mxt1))
print(dist2m_moyg(Mxa1,Mrt1))
print(dist2m_moyg(Mra1,Mxt1))
print(dist2m_moyg(Mra1,Mrt1))