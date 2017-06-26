import csv
import numpy as np

allOrdersCSVfile = 'CSV_FILES/orders.csv'
allOrdersReader = csv.DictReader(open(allOrdersCSVfile))
mapOfUsersByOrder = {}
mapOfOrdersByUser = {}
for row in allOrdersReader:
    currentUser = row['user_id']
    currentOrder = row['order_id']
    currentEvalSet = row['eval_set']
    if(currentEvalSet=='test'):
        mapOfUsersByOrder[currentOrder] = currentUser
        #VERIFIED NO REPEATS WITH BELOW COMMENTED CODE
        #if(currentUser in mapOfOrdersByUser):
        #    print("REPEAT!!!")
        mapOfOrdersByUser[currentUser] = currentOrder

priorTrainData = 'GENERATED_FILES/userProductPairsPriorTrain_csv.csv'
priorTrainBlockReader = csv.DictReader(open(priorTrainData))
TESTDATA_userID = []
TESTDATA_orderID = []
TESTDATA_productID = []
TESTDATA_numberProducts = []
displayIndex = 1.0
for row in priorTrainBlockReader:
    currentProductUser = row['userProduct_id']
    userAndProduct = currentProductUser.split("_")
    currentUser = userAndProduct[0]
    currentProduct = userAndProduct[1]
    if(currentUser in mapOfOrdersByUser):
        if(int(displayIndex)%100000==0):
            print(str(displayIndex/1000000.0) + " Million Rows Processed")
        TESTDATA_userID.append(currentUser)
        TESTDATA_orderID.append(mapOfOrdersByUser[currentUser])
        TESTDATA_productID.append(currentProduct)
        TESTDATA_numberProducts.append(int(row['number_orders']))
        displayIndex = displayIndex + 1

TESTDATA = np.zeros((len(TESTDATA_userID),4))
TESTDATA[:,0]=np.array(TESTDATA_userID)
TESTDATA[:,1]=np.array(TESTDATA_orderID)
TESTDATA[:,2]=np.array(TESTDATA_productID)
TESTDATA[:,3]=np.array(TESTDATA_numberProducts)

np.save('GENERATED_FILES/TESTING_X_DATA.npy',TESTDATA)