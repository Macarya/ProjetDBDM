import os

os.chdir("D:\\Users\\Yannis\\Documents\\ProjetDBDM")

from distance import *
from parsing import *

classifieur=Classifieur()
Lname=['lois','Yannis','Xavier','Angele','hugo','Emile','red']

for name in Lname:
    dur1,res1=parse('Records/'+name+'-phrase1.txt')
    dur2,res2=parse('Records/'+name+'-phrase2.txt')
    dur3,res3=parse('Records/'+name+'-phrase3.txt')
    res,dur=concatRes(res1),concatDuree(dur1)
    classifieur.addTraining(name,res)

"""for delta in [1,1.2,1.5,1.8,2,2.2,3]:
    score=0
    for name in Lname:
        for i in range(4,7):
            dur,res=parse('Records/'+name+'-phrase'+str(i)+'.txt')
            nameres=classifieur.predict(res,delta)
            if nameres==name:
                score+=1
    print(score)"""
        
"""for name in Lname:
    print(name+':')
    for i in range(4,7):
        dur,res=parse('Records/'+name+'-phrase'+str(i)+'.txt')
        print(classifieur.predictmoyap(res))
        print('\n')
    print('\n')"""