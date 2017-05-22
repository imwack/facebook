#coding=utf-8
import numpy as np
import pydotplus
from sklearn import preprocessing
from sklearn import tree
from sklearn.model_selection import train_test_split


if __name__=="__main__":
    # 读取特征
    featurePath = ".//feature//"+"facebook1000"
    labelPath = ".//feature//"+"facebook1000label"
    data = np.loadtxt(featurePath)
    target = np.loadtxt(labelPath)

    # 正则化特征
    print "MinMaxScaler..."
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    # print data

    # 分类
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.5, random_state = 42)
    clf = tree.DecisionTreeClassifier() # 决策树
    clf = clf.fit(X_train, y_train)

    print clf.score(X_test,y_test)
    y = clf.predict(X_test)
    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("DecisionTree.pdf")
    # 分析