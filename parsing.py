import os

#os.chdir("D:\\Users\\Yannis\\Documents\\ProjetDBDM")

def aff(res):
	for i in range(len(res)):
		for j in range(len(res[i])):
			if res[i][j]!=[]:
				print(i,j)


def parse(NomFichier='out.txt'):
	"""Parse un fichier d'entrée pour donner une matrice avec les temps d'écart par touche consécutive frappé (Resultat[cle1][cle2]) et la durée de pression de chaque touche (Dure[cle])"""
	with open(NomFichier,'r') as fichier:
		texte=fichier.read()
	texte=texte.split(',')[:-1]
	Resultat=[]
	for j in range(248):
		Resultat.append([ [] for i in range(248)])
	Duree=[ [] for i in range(248)]
	
	pkey,ptime=int(texte[0]),float(texte[2])
	Duree[pkey].append(-ptime)
	for n in range(3,len(texte),3):
		key,time=int(texte[n]),float(texte[n+2])
		if texte[n+1]=='+':
			Duree[key].append(-time)
			Resultat[pkey][key].append(time-ptime)
			pkey,ptime=key,time
		else:
			Duree[key][-1]+=time
	return(Duree,Resultat)



def concatDuree(*Duree):
	resDuree=[ [] for i in range(len(Duree[0]))]
	for dur in Duree:
		for i,t in enumerate(dur):
			for el in t:
				resDuree[i].append(el)
	return(resDuree)


def concatRes(*Res):
	finRes=[]
	for j in range(248):
		finRes.append([ [] for i in range(248)])
	for res in Res:
		for i,tt in enumerate(res):
			for j,t in enumerate(tt):
				for el in t:
					finRes[i][j].append(el)
	return(finRes)

