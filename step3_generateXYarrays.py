import csv
import numpy as np
#will do the initial training and validation of an XGBoost model

priorDataCSV = csv.DictReader(open('GENERATED_FILES/userProductPairsPrior_csv.csv'))
trainDataCSV = csv.DictReader(open('GENERATED_FILES/userProductPairsTrain_csv.csv'))

def generateMapFromCSV(csvFile):
    dataMap = {}
    displayIndex=1
    for row in csvFile:
        currentUserProduct = row['userProduct_id']
        currentNumOrder = row['number_orders']
        dataMap[currentUserProduct] = currentNumOrder
        if(displayIndex%100000==0):
            print(str(displayIndex/1000000.0) + ' million rows retrieved')
        displayIndex=displayIndex+1
    return dataMap

print("Now generating prior data")
XdataMap = generateMapFromCSV(priorDataCSV)

print("now generating train data")
YdataMap = generateMapFromCSV(trainDataCSV)

Xdata = np.zeros((len(XdataMap)))
yData = np.zeros((len(XdataMap)))

index=0
for userProd in XdataMap:
    Xdata[index]=XdataMap[userProd]
    if(userProd in YdataMap):
        yData[index]=YdataMap[userProd]
    else:
        yData[index]=0
    if (index % 100000 == 0):
        print(str(index / 1000000.0) + ' million rows generated')
    index = index + 1

np.save('GENERATED_FILES/Attempt1_Xdata.npy',Xdata)
np.save('GENERATED_FILES/Attempt1_yData.npy',yData)