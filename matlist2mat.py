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

def ll2m(L,f=moyenne):
    return [f(l) for l in L]


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
                if (M1[i][j]>M2[i][j]):
                    a+=M1[i][j]/M2[i][j]
                else :
                    a+=M2[i][j]/M1[i][j]
                k+=1
    if k > 0:
        return a/k
    return -1


def dist2l_moya(L1,L2):
    a = 0;
    k = 0;
    for i in range(len(L1)):
        if (L1[i]>0 and L2[i]>0):
            a+=abs(L1[i]-L2[i])
            k+=1
    if k > 0:
        return a/k
    return -1

def dist2l_moyg(L1,L2):
    a = 0;
    k = 0;
    for i in range(len(L1)):
        if (L1[i]>0 and L2[i]>0):
            if (L1[i]>L2[i]):
                a+=L1[i]/L2[i]
            else :
                a+=L2[i]/L1[i]
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

Lxa1[16] = -1
Lra1[16] = -1
Lxt1[16] = -1
Lrt1[16] = -1
Lxl1[16] = -1
Lxc1[16] = -1
Lxa1[9] = -1
Lra1[9] = -1
Lxt1[9] = -1
Lrt1[9] = -1
Lxl1[9] = -1
Lxc1[9] = -1

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