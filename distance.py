from matlist2mat import mtxl2m,dist2m_moyap
from math import sqrt

#Training matrice de paire (moyenne, ecart_type)
#Sample matrice de liste de temps
def distance(Training, Sample, delta):
	score = 0
	for i in range(len(Sample)):
		for j in range(len(Sample)):
			mean, std, long = Training[i][j]
			std = sqrt(std)
			min = mean - delta*std
			max = mean + delta*std
			for x in Sample[i][j]:
				if (x > min) and (x < max):
					score += 1
	return score

class Classifieur:
	def __init__(self):
		self.trainings = {}

	def addTraining(self, className, matrix):
		self.trainings[className] = mtxl2m(matrix)

	def predict(self, matrix, delta=1.2):
		maxi = -1
		best = ""
		for clas, clasMat in self.trainings.items():
			s = distance(clasMat, matrix, delta)
			if s > maxi:
				maxi = s
				best = clas
		return best

	def predictmoyap(self, matrix):
		maxi = 1000000
		best = ""
		for clas, clasMat in self.trainings.items():
			s = dist2m_moyap(clasMat, matrix)
			print(clas,s)
			if s < maxi:
				maxi = s
				best = clas
		return best

	def printing(self):
		print (self.trainings)

	def __repr__(self):
		return str(self.trainings)
