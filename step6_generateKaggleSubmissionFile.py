import numpy as np
import random
import time
import datetime
import csv

TEST_DATA_YRESULT = np.load('GENERATED_FILES/RAW_YRESULT.npy')
TEST_DATA_TABLE = np.load('GENERATED_FILES/TESTING_X_DATA.npy')

mapOfOrdersAndProducts = {}
for rowNum in range(len(TEST_DATA_YRESULT)):
    currentY = TEST_DATA_YRESULT[rowNum]

    if(rowNum%100000==0):
        print('Now Processing Result Row ' + str(rowNum/1000000.0) +
              ' of ' + str(len(TEST_DATA_YRESULT)/1000000.0) + ' million')

    #randomly decide based on number whether to include product
    if(random.random() < currentY):
        currentOrderId = TEST_DATA_TABLE[rowNum,1]
        currentProductId = TEST_DATA_TABLE[rowNum,2]
        if(currentOrderId not in mapOfOrdersAndProducts):
            mapOfOrdersAndProducts[currentOrderId] = []
        mapOfOrdersAndProducts[currentOrderId].append(currentProductId)


ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d__%H_%M_%S')
fileName = 'SUBMISSIONS/KaggleSubmissionGeneratedOn_' + st + '.csv'

def generateProductString(orderId):
    if(orderId in mapOfOrdersAndProducts):
        outputStr = ''
        for prodId in mapOfOrdersAndProducts[orderId]:
            outputStr = outputStr + ' ' + str(int(prodId))
        return outputStr[1:len(outputStr)]
    else:
        return 'None'

alreadyWrittenOrderIds = {}
with open(fileName, 'w') as csvfile:
    csvfile.write('order_id,products\n')
    for ind in range(TEST_DATA_TABLE.shape[0]):

        if (ind % 500000 == 0):
            print('Now Writing Data From Row ' + str(ind / 1000000.0) +
                  ' of ' + str(TEST_DATA_TABLE.shape[0] / 1000000.0) + ' million')

        orderId = TEST_DATA_TABLE[ind,1]
        if(orderId not in alreadyWrittenOrderIds):
            currentRow = str(int(orderId))+","+str(generateProductString(orderId))+'\n'
            alreadyWrittenOrderIds[orderId]=1
            csvfile.write(currentRow)