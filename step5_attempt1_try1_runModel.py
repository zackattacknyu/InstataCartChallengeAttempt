import xgboost as xgb
import numpy as np
import csv

def addConstColumn(initalTable):
    outputTable = np.ones((initalTable.shape[0],2))
    outputTable[:,0]=initalTable
    return outputTable

TEST_DATA_TABLE = np.load('GENERATED_FILES/TESTING_X_DATA.npy')
TEST_DATA_XINPUT = addConstColumn(TEST_DATA_TABLE[:,3])

xData80A = np.load('GENERATED_FILES/Attempt1_Split1_xData80.npy')
xData20A = np.load('GENERATED_FILES/Attempt1_Split1_xData20.npy')
yData80 = np.load('GENERATED_FILES/Attempt1_Split1_yData80.npy')
yData20 = np.load('GENERATED_FILES/Attempt1_Split1_yData20.npy')

xData80 = addConstColumn(xData80A)
xData20 = addConstColumn(xData20A)

numZero = float(len(np.array(np.where(yData20<1))[0]))
numOne = float(len(np.array(np.where(yData20>0))[0]))
allZerosPred = np.zeros((len(yData20)))
maeAllZeros = np.sum( np.abs(yData20-allZerosPred) )/len(yData20)

clf = xgb.XGBRegressor(max_depth=3,
                           n_estimators=150,
                           min_child_weight=9,
                           learning_rate=0.05,
                           nthread=8,
                           subsample=0.80,
                           colsample_bytree=0.80,
                           seed=4242)

clf.fit(xData80, yData80, eval_set=[(xData20, yData20)], verbose=True,
        eval_metric='mae', early_stopping_rounds=100)

print("MAE if predict all zeros: " + str(maeAllZeros))

TEST_DATA_YRESULT = clf.predict(TEST_DATA_XINPUT)
np.save('RAW_YRESULT.npy',TEST_DATA_YRESULT)

