#coding=utf-8

from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from randomForest import *

if __name__ == "__main__":
    fpath = os.getcwd()+"\\feature\\feature.txt"
    lpath = os.getcwd()+"\\feature\\label.txt"
    f,l = readFile(fpath,lpath)
    feature = np.array(f)
    label = np.array(l).reshape((-1, 1))
    # print label.shape
    # print label,feature
    # 拆分训练集和测试集
    feature_train, feature_test, target_train, target_test = train_test_split(feature, label, test_size=0.5,
                                                                              random_state=0)
    clf = tree.DecisionTreeClassifier(random_state=0,criterion='entropy')
    clf.fit(feature_train,target_train)

    r = clf.score(feature_test, target_test)
    # print "accuracy:",r

    result = clf.predict(feature_test)
    # print(feature_test)
    # print(target_test)
    # print(result)
    print(np.mean(result == target_test))
    print accuracy_score(target_test, result)
    with open("DecisionTree.dot", 'w') as f:
        f = export_graphviz(clf, out_file=f)

    '''''准确率与召回率'''
    precision, recall, thresholds = precision_recall_curve(target_train, clf.predict(feature_train))

    answer = clf.predict_proba(feature)[:, 1]
    print(classification_report(label, answer, target_names=['thin', 'fat']))