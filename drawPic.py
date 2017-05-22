#coding=utf-8
from snap import *
from featureExtract import *
import matplotlib.pyplot as plt

def GetDegree(G):
    degree_number = {}
    for NI in G.Nodes():
        deg = NI.GetDeg()
        if degree_number.has_key(deg):
            degree_number[deg]+=1
        else:
            degree_number[deg] = 1
    return degree_number


def plotDegree(degree_number={}):

    # degree_number = sorted(degree_number.iteritems(), key=lambda d:d[1], reverse = True)
    print degree_number
    s = sum(degree_number.keys())
    k = degree_number.keys()
    val = degree_number.values()
    y = [v / float(sum(val)) for v in val]
    #vv = [vi*1.0/s for vi in v]
    # plt.plot(k, y, '.')
    plt.loglog(k,y,'.')
    # plt.title("出度-频度分布图", fontproperties=myfont)
    # plt.xlabel("出度", fontproperties=myfont)
    # plt.ylabel("频度", fontproperties=myfont)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    FIn = snap.TFIn("./graph/Wiki-Vote400.graph")
    G = snap.TNGraph.Load(FIn)

    degree_number = GetDegree(G)       #degree-number dic
    plotDegree(degree_number)

    # PlotClustCf(G, "example", "Directed graph - clustering coefficient")
    # PlotOutDegDistr(G, "example", "Undirected graph - out-degree Distribution")




