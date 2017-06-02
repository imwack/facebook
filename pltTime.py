#coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pylab import mpl
import numpy as np
import panda as pd
from itertools import cycle

# 5000node  5253.83599997   5183.4059999
# 4000      4468.24099994   2940.92799997
# 3000      2670.11100006   1786.24199986
# 2000      1309.29999995   968.773000002
# 1000      304.3349998     208.134000063

t5000 = 5183.4059999
t4000 = 2940.92799997
t3000 = 1786.24199986
t2000 = 968.773000002
t1000 = 208.134000063

def plotLOF():
    x = [1000, 2000, 3000, 4000, 5000]
    y = [208.134000063, 908.773000002, 1786.24199986, 2940.92799997, 5183.4059999]
    y1 = [355.562999964,1444.28500009,3296.91100001, 5650.85800004,10085.003]
    # ax = plt.subplot(1,1,1)
    ax = plt.subplot(111)
    # ax.xaxis.set_major_locator(xmajorLocator)
    # ax.yaxis.set_major_locator(ymajorLocator)
    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度

    # plt.plot(x, y, color="blue", linestyle="-", label="cosine")
    line1 = ax.plot(x, y, 'b.-',label="LOF_k=1")
    line2 = ax.plot(x, y1, 'r.-',label="LOF_k=3")
    plt.legend(loc='upper left')
    # ax.legend(line1, ('LOF-7d',))  # 多加一个逗号
    # plt.title("Lof Detection Time")
    plt.xlabel("nodes")
    plt.ylabel("time(s)")
    plt.show()

def plotFeatureExtract():

    x = [4039,7115,10000,22687,36692]
    x2 = [i*1.0/10000 for i in x]
    y = [63,125,278,579,2683]
    t = [0.451,0.575,0.610,0.912,1.394]
    t1 = [0.161,0.314,0.316,0.941,3.589]
    # ax = plt.subplot(1,1,1)
    ax = plt.subplot(1,2,1)
    # ax.xaxis.set_major_locator(xmajorLocator)
    # ax.yaxis.set_major_locator(ymajorLocator)
    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    #plt.plot(x, y, color="blue", linestyle="-", label="cosine")
    line1 = ax.plot(x, y, 'b.',label="Feature Extract Time")

    # title("a strait line")
    plt.xlabel("Nodes")
    plt.ylabel("Time(s)")
    # y = 0.0759*x - 476.6504
    x1 = [ i for i in range(0,40000) ]
    y1 = [0.08*i - 476.6504 for i in range(0,40000) ]
    line2 = ax.plot(x1,y1,'r-',label="y=0.08x-476.6504")
    plt.legend(loc='upper left')
    # ax.legend([line1,line2],['Feature Extract Time', 'y=0.08x-476.6504'])  # 多加一个逗号

    ax = plt.subplot(1,2,2)
    # ax.xaxis.set_major_locator(xmajorLocator)
    # ax.yaxis.set_major_locator(ymajorLocator)
    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度

    #plt.plot(x, y, color="blue", linestyle="-", label="cosine")
    line1 = ax.plot(x2, t, 'b.',label="GBKD-Forest Classification")
    # line3 = ax.plot(x2,t1,'bx',label="SVM Classification")
    # ax.legend(line1, ('Classification Time',))  # 多加一个逗号
    # title("a strait line")
    x1 = [ i for i in range(0,5) ]
    y1 = [0.28*i +0.3397 for i in range(0,5) ]
    line2 = ax.plot(x1,y1,'r-',label="y=0.28x+0.3397")
    #line4 = ax.plot(x1, y2, 'b-', label="y=0.4288x^2-0.7467x+0.5277")
    plt.legend(loc='upper left')
    plt.xlabel("Nodes(10k)")
    plt.ylabel("Time(s)")
    plt.suptitle("Feature Extract & Classification Time")
    plt.show()


def plotPrecision():
    path  = "precision"
    data = []
    f = open(path,'r')
    for line in f:
        temp = line.split('\t')
        for i in range(len(temp)):
            try:
                temp[i] = float(temp[i])
            except:
                print i,temp[i]


        data.append(temp)
    #data = np.array(data)
    for i in range(len(data)):
        data[i] = data[i][:-1]
    print data[0]
    print data[1]
    #print len(data[0]),len(data[1]),len(data[2]),len(data[3]),len(data[4]),len(data[5]),len(data[6]),len(data[7]),len(data[8]),len(data[9])

    x = [i for i in range(11)]
    for i in range(11):
        x[i] = x[i]*1.0/10
    colors = ['navy', 'turquoise', 'darkorange', 'cornflowerblue', 'teal','black']
    plt.plot(data[1], data[0], color=colors[0], label="Facebook")
    plt.plot(data[3], data[2], color=colors[1], label="Wiki-Vote")
    plt.plot(data[5], data[4], color=colors[2], label="Synthetic")
    plt.plot(data[7], data[6], color=colors[3], label="Gnutella-P2P")
    plt.plot(data[9], data[8], color=colors[4], label="Email-Enron")
    plt.plot(x,x,color=colors[5],label="y=x")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall curve of GBKD-Forest')
    plt.legend(loc="lower right")
    plt.show()


if __name__=="__main__":
    #plotPrecision()
    #plotLOF()
    plotFeatureExtract()