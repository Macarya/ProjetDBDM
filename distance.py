from matlist2mat import mtxl2m
from math import sqrt

#Training matrice de paire (moyenne, ecart_type)
#Sample matrice de liste de temps
def distance(Training, Sample):
	score = 0
	for i in range(len(Sample)):
		for j in range(len(Sample)):
			mean, std = Training[i][j]
			std = sqrt(std)
			min = mean - 1.5*std
			max = mean + 1.5*std
			for x in Sample[i][j]:
				if (x > min) and (x < max):
					score += 1
	return score

class Classifieur:
	def __init__(self):
		self.trainings = {}

	def addTraining(self, className, matrix):
		self.trainings[className] = mtxl2m(matrix)

	def predict(self, matrix):
		maxi = -1
		best = ""
		for clas, clasMat in self.trainings.items():
			s = distance(clasMat, matrix)
			if s > maxi:
				maxi = s
				best = clas
		return best

	def printing(self):
		print (self.trainings)

	def __repr__(self):
		return str(self.trainings)
