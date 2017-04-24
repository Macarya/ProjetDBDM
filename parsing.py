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
    
    
