#coding=utf-8
import os
import numpy as np
from sklearn.metrics import *
from sklearn import metrics

if __name__=="__main__":
    number = 1000
    filename = "lof_result_feature10000_1000.txt"
    path = os.getcwd() + "\\feature\\label.txt"
    lable = []
    with open(path,'r') as f:
        for line in f:
            lable.append(int(line))

    lable = lable[:number]
    anomaly=0
    for i in lable:
        if i==1:
            anomaly+=1
    print anomaly
    # print lable

    ind = []
    score = []
    with open(filename,'r') as f:
        for line in f:
            lst = line.split('\t')
            ind.append(int(lst[0]))
            score.append(float(lst[2]))
    # print ind
    # print score
    lof = [0 for i in range(0,number)]
    # print lof
    length = len(ind)
    for i in range(anomaly):
        lof[ind[i]] = 1


    count = 0
    for i in range(number):
        if lable[i]==lof[i]:
            count+=1
    y_true = np.array(lable)
    y_scores = np.array(lof)
    y_pred = y_scores
    print average_precision_score(y_true, y_scores)
    print accuracy_score(y_true, y_scores)
    print recall_score(y_true, y_pred, average='binary')
    print f1_score(y_true, y_pred, average='binary')

    fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred, pos_label=1)
    #print fpr,tpr
    print metrics.auc(fpr, tpr)


