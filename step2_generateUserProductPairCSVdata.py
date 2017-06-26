import numpy as np
import csv

priorDataFile = 'GENERATED_FILES/userProductPairsPrior.txt'
priorDataOutputFile = 'GENERATED_FILES/userProductPairsPrior_csv.csv'

#priorDataFile = 'GENERATED_FILES/userProductPairsTrain.txt'
#priorDataOutputFile = 'GENERATED_FILES/userProductPairsTrain_csv.csv'

userProductPairs = {}

with open(priorDataFile,'r') as file1:
    for pair1 in file1:
        pair = pair1.strip()
        if(pair not in userProductPairs):
            userProductPairs[pair]=0
        userProductPairs[pair] = userProductPairs[pair]+1

outputCSVfile = open(priorDataOutputFile,"w")
userProductCSVfile = csv.DictWriter(outputCSVfile,fieldnames=['userProduct_id','number_orders'])
userProductCSVfile.writeheader()

numberPairs = str(len(userProductPairs)/1000000.0)
numberPairsTrunc = numberPairs[0:4]

displayIndex=1
for userProdPair in userProductPairs:
    currentDict = {}
    currentDict['userProduct_id']=userProdPair
    currentDict['number_orders']=userProductPairs[userProdPair]
    userProductCSVfile.writerow(currentDict)
    if(displayIndex%100000==0):
        disp = str(displayIndex/1000000.0)
        disp1 = disp[0:4]
        print("Printed CSV Row " + disp1 + " of " + numberPairsTrunc + " million")
    displayIndex = displayIndex+1

outputCSVfile.close()
