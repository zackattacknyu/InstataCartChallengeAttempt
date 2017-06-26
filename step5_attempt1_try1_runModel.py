#import xgboost as xgb
import numpy as np
import csv


#TESTDATA_numberProductsArr = np.array(TESTDATA_numberProducts)
#TESTDATA_numProductsX = np.ones((TESTDATA_numberProductsArr.shape[0],2))
#TESTDATA_numProductsX[:,0] = TESTDATA_numberProductsArr

#print(TESTDATA_numProductsX.shape)
"""
xData80A = np.load('GENERATED_FILES/Attempt1_Split1_xData80.npy')
xData20A = np.load('GENERATED_FILES/Attempt1_Split1_xData20.npy')
yData80 = np.load('GENERATED_FILES/Attempt1_Split1_yData80.npy')
yData20 = np.load('GENERATED_FILES/Attempt1_Split1_yData20.npy')

xData80 = np.ones((xData80A.shape[0],2))
xData80[:,0]=xData80A
xData20 = np.ones((xData20A.shape[0],2))
xData20[:,0]=xData20A

numZero = float(len(np.array(np.where(yData20<1))[0]))
numOne = float(len(np.array(np.where(yData20>0))[0]))
allZerosPred = np.zeros((len(yData20)))
maeAllZeros = np.sum( np.abs(yData20-allZerosPred) )/len(yData20)

clf = xgb.XGBRegressor(max_depth=3,
                           n_estimators=1500,
                           min_child_weight=9,
                           learning_rate=0.05,
                           nthread=8,
                           subsample=0.80,
                           colsample_bytree=0.80,
                           seed=4242)

clf.fit(xData80, yData80, eval_set=[(xData20, yData20)], verbose=True,
        eval_metric='mae', early_stopping_rounds=100)

print("MAE if predict all zeros: " + str(maeAllZeros))

"""