#coding=utf-8
import snap
from featureExtract import *
import matplotlib.pyplot as plt
from pylab import *

def plotDegree(degree_number={}):
    s = sum(degree_number.keys())
    k = degree_number.keys()
    v = degree_number.values()
    print sorted(degree_number.iteritems(), key=lambda d:d[1], reverse = True)
    #vv = [vi*1.0/s for vi in v]
    plt.plot(k, v, '.')
    # plt.title("出度-频度分布图", fontproperties=myfont)
    # plt.xlabel("出度", fontproperties=myfont)
    # plt.ylabel("频度", fontproperties=myfont)
    plt.grid(True)
    plt.show()