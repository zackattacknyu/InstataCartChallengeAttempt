import numpy as np
#import matplotlib.pyplot as plt
from sklearn import model_selection

XX = np.load('GENERATED_FILES/Attempt1_Xdata.npy')
yy = np.load('GENERATED_FILES/Attempt1_yData.npy')

xData80, xData20, yData80, yData20 = model_selection.train_test_split(
    XX, yy, random_state=42,stratify=yy,test_size=0.2)

np.save('GENERATED_FILES/Attempt1_Split1_xData80.npy',xData80)
np.save('GENERATED_FILES/Attempt1_Split1_xData20.npy',xData20)
np.save('GENERATED_FILES/Attempt1_Split1_yData80.npy',yData80)
np.save('GENERATED_FILES/Attempt1_Split1_yData20.npy',yData20)