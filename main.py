#coding=utf-8
import numpy
from sklearn import preprocessing

if __name__=="__main__":
    # 读取特征
    featurePath = ".//feature//"+"facebook1000"
    labelPath = ".//feature//"+"facebook1000label"
    data = numpy.loadtxt(featurePath)
    target = numpy.loadtxt(labelPath)

    # 正则化特征
    print "MinMaxScaler..."
    min_max_scaler = preprocessing.MinMaxScaler()
    data = min_max_scaler.fit_transform(data)
    print data

    # 分类

    # 分析