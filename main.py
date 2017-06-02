#coding=utf-8
import numpy as np
import pydotplus
from sklearn import preprocessing
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time


n_classes = 2
plot_colors = "bry"
plot_step = 0.02

if __name__=="__main__":
    t1 = time.time()
    # 读取特征
    featurePath = ".//feature//"+"EmailEnron2000"
    labelPath = ".//feature//"+"EmailEnron2000label"
    data = np.loadtxt(featurePath)
    target = np.loadtxt(labelPath)
    data = np.delete(data,3,axis=1)

    feature_names = ["InDegree","OutDegree","PageRank","Closeness","Hubs","Authority","Ego-OutNodes","Ego-Nodes","Ego-Edges"]
    target_names = ["normal","anomaly"]
    # 正则化特征
    print "MinMaxScaler..."
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    # print data

    # 分类
    print "train_test_split..."
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.5, random_state = 10)
    # X_train = data[:len(data)/2]
    # X_test = data[len(data)/2:]
    # y_train = target[:len(target) / 2]
    # y_test = target[len(target) / 2:]
    print X_train.shape,X_test.shape,y_train.shape,y_test.shape

    clf = tree.DecisionTreeClassifier(criterion="gini",max_depth=4) # 决策树entropy
    clf = clf.fit(X_train, y_train)

    print clf.score(X_test,y_test)
    y = clf.predict(X_test)
    count = 0
    for i in range(len(y)):
        if y[i]==y_test[i]:
            count+=1
    print count,len(y)
    t2 = time.time()

    print t2-t1
    dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names = feature_names,
                                    class_names = target_names,
                                    filled=True, rounded=True,)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("DecisionTree.pdf")
    # 分析

    '''
    for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],[0,4],[0,5],[0,6],[0,7],[0,8],
                                    [1, 2], [1, 3],[1,4],[1,5],[1,6],[1,7],[1,8],
                                    [2, 3],[2,4],[2,5],[2,6],[2,7],[2,8],
                                    [3,4],[3,5],[3,6],[3,7],[3,8],[4,5],[4,6],[4,7],[4,8],
                                    [5,6],[5,7],[5,8],[6,7],[6,8],[7,8]
                                    ]):
        # We only take the two corresponding features
        X = data[:, pair]
        y = target

        # Train
        clf = tree.DecisionTreeClassifier().fit(X, y)

        # Plot the decision boundary
        plt.subplot(9, 4, pairidx + 1)

        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                             np.arange(y_min, y_max, plot_step))

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

        plt.xlabel(feature_names[pair[0]])
        plt.ylabel(feature_names[pair[1]])
        plt.axis("tight")

        # Plot the training points
        for i, color in zip(range(n_classes), plot_colors):
            idx = np.where(y == i)
            plt.scatter(X[idx, 0], X[idx, 1], c=color, label=target_names[i],
                        cmap=plt.cm.Paired)

        plt.axis("tight")

    plt.suptitle("Decision surface of a decision tree using paired features")
    plt.legend()
    plt.show()
    '''