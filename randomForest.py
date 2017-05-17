#coding=utf-8
from snap import *
import numpy as np
from featureExtract import *
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
from sklearn.externals.joblib import Parallel, delayed
from sklearn.externals.six import StringIO
import matplotlib.pyplot as plt
from pltUtil import *
import pydot
import os


def split_data(feature, label):
    n = -400
    feature_train = feature[n:-20]
    feature_test = feature[0:n]
    target_train = label[n:-20]
    target_test = label[0:n]
    for i in range(-20,0):
        feature_test.append(feature[i])
        target_test.append(label[i])
    print len(feature_train),len(feature_test)
    # only 40 anomaly
    return feature_train, feature_test, target_train, target_test


def readFile(fpath,lpath):
    feature = []
    label = []
    data = []
    f = open(fpath,'r')
    l = open(lpath,'r')

    data = [line.strip().split('\t') for line in f]
    feature = [[float(x) for x in row[1:]] for row in data]

    try:
        for line in l:
            la = line.strip()
            label.append(int(la))
    finally:
        l.close()

    #print len(feature),len(feature[0])
    return feature,label


if __name__ == '__main__':
    fpath = os.getcwd()+"\\feature\\facebook1000_feature.txt"   # 特征
    lpath = os.getcwd()+"\\feature\\facebook1000_label.txt"                  # 标签
    f,l = readFile(fpath,lpath)
    feature = np.array(f)
    label = np.array(l).reshape((-1,1))
    # print label.shape
    # print label,feature
    # 拆分训练集和测试集
    feature_train, feature_test, target_train, target_test = train_test_split(feature, label, test_size=0.8, random_state=1)

    # feature_train, feature_test, target_train, target_test = split_data(f,l)

    # print len(feature_train),len(feature_test)

    #print feature_train.shape,target_train.shape

    clf = RandomForestClassifier(n_estimators=5)    # 5 tree

    # 训练模型
    s = clf.fit(feature_train, target_train.ravel())
    #print s

    # 评估模型准确率
    r = clf.score(feature_test, target_test)
    print "accuracy:",r

    print 'Predict class：\n %s' % clf.predict(feature_test)
    result = clf.predict(feature_test)
    # print target_test.reshape((1,-1))
    e = target_test.reshape((1,-1))[0]
    print e

    print(np.mean(e == target_test))

    f = open('result.txt','w')
    for i in range(len(e)):
        # print res[i]
        f.write(str(result[i]))
        f.write('\t')
        f.write(str(e[i]))
        f.write('\n')
    f.close()
    '''
    print clf.predict_proba(feature_test)
    lst = clf.predict_proba(feature_test)

    #print 'list of DecisionTreeClassifier:%s' % clf.estimators_

    # print clf.classes_
    # print clf.n_classes_

    print 'feature importance：%s' % clf.feature_importances_

    print clf.n_outputs_    #The number of outputs when fit is performed.


    def _parallel_helper(obj, methodname, *args, **kwargs):
        return getattr(obj, methodname)(*args, **kwargs)


    all_proba = Parallel(n_jobs=10, verbose=clf.verbose, backend="threading")(
        delayed(_parallel_helper)(e, 'predict_proba', feature_test) for e in clf.estimators_)
    print '所有树的判定结果：%s' % all_proba

    proba = all_proba[0]
    for j in range(1, len(all_proba)):
        proba += all_proba[j]
    proba /= len(clf.estimators_)
    print '数的棵树：%s ， 判不作弊的树比例：%s' % (clf.n_estimators, proba[0, 0])
    print '数的棵树：%s ， 判作弊的树比例：%s' % (clf.n_estimators, proba[0, 1])

    # 当判作弊的树多余不判作弊的树时，最终结果是判作弊
    print '判断结果：%s' % clf.classes_.take(np.argmax(proba, axis=1), axis=0)
    '''
    # 把所有的树都保存到word
    for i in xrange(len(clf.estimators_)):
        export_graphviz(clf.estimators_[i], '%d.dot' % i)
        # cmd = "dot -Tpdf %d.dot -o %d.pfd" % (i,i)
        # os.system(cmd)
