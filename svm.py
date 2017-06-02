#coding=utf-8
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time
from sklearn.metrics import *
from sklearn import preprocessing

if __name__ == '__main__':
    t1 = time.time()
    # 读取特征
    featurePath = ".//feature//" + "facebook400"
    labelPath = ".//feature//" + "facebook400label"
    data = np.loadtxt(featurePath)
    target = np.loadtxt(labelPath)
    for i in range(len(target)):
        if target[i] == 1:
            target[i] = 0
        else:
            target[i] = 1
    data = np.delete(data, 3, axis=1)
    print data.shape
    feature_names = ["InDegree", "OutDegree", "PageRank", "Closeness", "Hubs", "Authority", "Eccentricity", "EgoOutD",
                     "EgoNodes", "EgoEdges"]
    target_names = ["normal", "anomaly"]
    # 正则化特征
    print "MinMaxScaler..."
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    # print data

    # 分类
    print "train_test_split..."
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.6, random_state=10)
    clf = svm.SVC()
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    score = clf.score(X_test,y_test)

    t2 = time.time()
    print average_precision_score(y_test,y_pred)
    print accuracy_score(y_test, y_pred)
    print recall_score(y_test, y_pred, average='binary')
    print f1_score(y_test, y_pred, average='binary')
    fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=1)
    # print fpr,tpr
    # plt.plot(fpr,tpr,'-')
    # plt.show()
    # print fpr,tpr
    print auc(fpr, tpr)
    print "time:",t2-t1