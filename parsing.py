

with open('out.txt','r') as fichier:
    texte=fichier.read()
    
texte=texte.split(',')
Resultat=[]
for j in range(123):
    Resultat.append([ [] for i in range(123)])
Duree=[ [] for i in range(123)]

pkey,ptime=int(texte[0]),float(texte[2])
Duree[pkey].append(ptime)
for n in range(3,len(texte),3):
    if texte[n]=='\n':
        break
    key,time=int(texte[n]),float(texte[n+2])
    if texte[n+1]=='+':
        Duree[key].append(-time)
        Resultat[pkey][key].append(time-ptime)
    else:
        Duree[key][-1]+=time
    
    
