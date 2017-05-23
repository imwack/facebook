#coding=utf-8
import numpy as np
import pydotplus
from sklearn import preprocessing
from sklearn import tree
from sklearn.model_selection import train_test_split


if __name__=="__main__":
    # 读取特征
    featurePath = ".//feature//"+"EmailEnron2000"
    labelPath = ".//feature//"+"EmailEnron2000label"
    data = np.loadtxt(featurePath)
    target = np.loadtxt(labelPath)

    # 正则化特征
    print "MinMaxScaler..."
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    # print data

    # 分类
    print "train_test_split..."
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.5, random_state = 0)
    # X_train = data[:len(data)/2]
    # X_test = data[len(data)/2:]
    # y_train = target[:len(target) / 2]
    # y_test = target[len(target) / 2:]
    print X_train.shape,X_test.shape,y_train.shape,y_test.shape

    clf = tree.DecisionTreeClassifier(max_depth=4) # 决策树
    clf = clf.fit(X_train, y_train)

    print clf.score(X_test,y_test)
    y = clf.predict(X_test)
    count = 0
    for i in range(len(y)):
        if y[i]==y_test[i]:
            count+=1
    print count,len(y)

    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("DecisionTree.pdf")
    # 分析