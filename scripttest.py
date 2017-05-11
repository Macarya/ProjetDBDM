import os

os.chdir("D:\\Users\\Yannis\\Documents\\ProjetDBDM")

from distance import *
from parsing import *

classifieur=Classifieur()
Lname=['lois']

for name in Lname:
    dur1,res1=parse('Records/'+name+'-Phrase1.txt')
    dur2,res2=parse('Records/'+name+'-Phrase2.txt')
    dur3,res3=parse('Records/'+name+'-Phrase3.txt')
    res,dur=concatRes(res1),concatDuree(dur1)
    classifieur.addTraining(name,res)

for name in Lname:
    for i in range(4,7):
        dur,res=parse('Records/'+name+'-Phrase'+str(i)+'.txt')
        classifieur.predict(res)