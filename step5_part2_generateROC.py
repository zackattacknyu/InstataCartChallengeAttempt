from sklearn.metrics import roc_curve,auc,accuracy_score
import numpy as np
import matplotlib.pyplot as plt

yHatValid = np.load('GENERATED_FILES/YHAT_VALID.npy')
yValidActual = np.load('GENERATED_FILES/Attempt1_Split1_yData20.npy')

fpr, tpr, thresholds = roc_curve(yValidActual, yHatValid)
roc_auc = auc(fpr, tpr)

print(thresholds)

accuracyScores = []
for thresh in thresholds:
    curScore = accuracy_score(yValidActual,yHatValid>thresh)
    accuracyScores.append(curScore)

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

plt.figure()
plt.plot(thresholds,tpr,color='red',label='True Positive')
plt.plot(thresholds,fpr,color='black',label='False Positive')
plt.plot(thresholds,accuracyScores,color='orange',lw=2,label='Accuracy')
plt.xlabel('Thresholds')
plt.ylabel('Rate')
plt.legend()
plt.show()