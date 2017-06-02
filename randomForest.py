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
    for i in range(len(target)):
        if target[i]==1:
            target[i]=0
        else:
            target[i]=1
    data = np.delete(data,3,axis=1)
    print data.shape
    feature_names = ["InDegree","OutDegree","PageRank","Closeness","Hubs","Authority","Eccentricity","EgoOutD","EgoNodes","EgoEdges"]
    target_names = ["normal","anomaly"]
    # 正则化特征
    print "MinMaxScaler..."
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    # print data

    # 分类
    print "train_test_split..."
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.8, random_state = 10)
    # X_train = data[:len(data)/2]
    # X_test = data[len(data)/2:]
    # y_train = target[:len(target) / 2]
    # y_test = target[len(target) / 2:]
    # print X_train.shape,X_test.shape,y_train.shape,y_test.shape

    clf = RandomForestClassifier(n_estimators=6,criterion="gini",max_depth=4)
    clf = clf.fit(X_train, y_train)

    # print clf.score(X_test,y_test)
    y_pred = clf.predict(X_test)
    y_score = clf.predict_proba(X_test)
    y_socre1 = y_score
    y_score = y_score[:,0]
    y_score.reshape(len(y_score),1)
    t2 = time.time()
    print "time:",t2-t1
    # 分析
    print average_precision_score(y_test,y_score)
    print accuracy_score(y_test, y_pred)
    print recall_score(y_test, y_pred, average='binary')
    print f1_score(y_test, y_pred, average='binary')
    fpr, tpr, thresholds = roc_curve(y_test, y_score, pos_label=0)
    # print fpr,tpr
    # plt.plot(fpr,tpr,'-')
    # plt.show()
    print auc(fpr, tpr)

    importances = clf.feature_importances_


    #Precision recall

    # Compute Precision-Recall and plot curve
    precision = dict()
    recall = dict()
    average_precision = dict()

    precision["micro"], recall["micro"], _ = precision_recall_curve(y_test.ravel(),
                                                                    y_score.ravel())
    average_precision["micro"] = average_precision_score(y_test, y_score,
                                                         average="micro")

    # print precision["micro"], recall["micro"]
    f = open("precision","a")
    for p in precision["micro"]:
        f.write(str(p))
        f.write("\t")
    f.write("\n")
    for p in recall["micro"]:
        f.write(str(p))
        f.write("\t")
    f.write("\n")
    f.close()
    # Plot Precision-Recall curve for each class
    plt.clf()
    plt.plot(recall["micro"], precision["micro"], color='gold', #lw=2,
             label='micro-average Precision-recall curve (area = {0:0.2f})'
                   ''.format(average_precision["micro"]))
    # for i, color in zip(range(n_classes), colors):
    #     plt.plot(recall[i], precision[i], color=color, lw=lw,
    #              label='Precision-recall curve of class {0} (area = {1:0.2f})'
    #                    ''.format(i, average_precision[i]))

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Extension of Precision-Recall curve to multi-class')
    plt.legend(loc="lower right")
    plt.show()


    '''
    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Feature importances of Directed Graph")
    indices = [i for i in range(len(feature_names))]
    plt.bar(indices,importances,
            color="r", align="center")
    plt.xticks(range(len(feature_names)), feature_names,rotation=30)
    plt.xlim([-1, len(feature_names)])
    plt.show()

    for i in xrange(len(clf.estimators_)):
        dot_data = export_graphviz(clf.estimators_[i], out_file=None,
                                        feature_names = feature_names,
                                        class_names = target_names,
                                        filled=True, rounded=True,)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf("DecisionTree %d.pdf" %i)
    '''

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