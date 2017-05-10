#Training matrice de paire (moyenne, ecart_type)
#Sample matrice de liste de temps
def distance(Training, Sample):
	score = 0
	for i in range(len(Sample)):
		for j in range(len(Sample)):
			mean, std = Training[i][j]
			min = mean - 1.5*std
			max = mean + 1.5*std
			for x in Sample[i][j]:
				if (x > min) and (x < max):
					score += 1
	return score

