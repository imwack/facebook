#coding=utf-8
import numpy as np
import pydotplus
from sklearn import preprocessing
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time
from sklearn.metrics import *
from sklearn.tree import export_graphviz

if __name__ == '__main__':
    featurePath = ".//feature//" + "facebook200"
    labelPath = ".//feature//" + "facebook200label"
    data = np.loadtxt(featurePath)
    target = np.loadtxt(labelPath)
    data = data[:,3]
    data = data.reshape(len(data),1)
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)

    y_test = target
    y_score = data
    y_pred = []

    yuzhi = sorted(data)[2000]
    print yuzhi
    for d in data:
        if d>yuzhi:
            y_pred.append(0)
        else:
            y_pred.append(1)

    print average_precision_score(y_test,y_score)
    print accuracy_score(y_test, y_pred)
    print recall_score(y_test, y_pred, average='binary')
    print f1_score(y_test, y_pred, average='binary')
    fpr, tpr, thresholds = roc_curve(y_test, y_score, pos_label=1)
    # print fpr,tpr
    # plt.plot(fpr,tpr,'-')
    # plt.show()
    print auc(fpr, tpr)