#coding=utf-8
from snap import *
import numpy as np
from featureExtract import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
from sklearn.externals.joblib import Parallel, delayed
from sklearn.externals.six import StringIO
import matplotlib.pyplot as plt
from pltUtil import *
import pydot
import os

def readFile():
    feature = []
    label = []
    data = []
    fpath = os.getcwd()+"\\feature\\feature.txt"
    lpath = os.getcwd()+"\\feature\\label.txt"
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
    f,l = readFile()
    feature = np.array(f)
    label = np.array(l).reshape((-1,1))
    # print label.shape
    # print label,feature
    # 拆分训练集和测试集
    feature_train, feature_test, target_train, target_test = train_test_split(feature, label, test_size=0.5, random_state=0)
    # print len(feature_train),len(feature_test)
    # 分类型决策树
    print feature_train.shape,target_train.shape

    clf = RandomForestClassifier(n_estimators=8)

    # 训练模型
    s = clf.fit(feature_train, target_train.ravel())
    #print s

    # 评估模型准确率
    r = clf.score(feature_test, target_test)
    print "score:",r

    print '判定结果：%s' % clf.predict(feature_test)
    print clf.predict_proba(feature_test)
    lst = clf.predict_proba(feature_test)

    #print 'list of DecisionTreeClassifier:%s' % clf.estimators_

    # print clf.classes_
    # print clf.n_classes_

    print 'feature importance：%s' % clf.feature_importances_

    print clf.n_outputs_


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

    # 把所有的树都保存到word
    for i in xrange(len(clf.estimators_)):
        export_graphviz(clf.estimators_[i], '%d.dot' % i)
        # cmd = "dot -Tpdf %d.dot -o %d.pfd" % (i,i)
        # os.system(cmd)
