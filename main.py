#coding=utf-8
from snap import *
from featureExtract import *
import matplotlib.pyplot as plt
from pltUtil import *


if __name__ == '__main__':
    G = FeatureExtract(40)
    degree_number = GetDegree(G)       #degree-number dic
    plotDegree(degree_number)


    # GetNodeDegree(G)
    # GetPageRank(G)
    # GetHits(G)
    # GetDegreeCentr(G)
    # GetBetweennessCentr(G)
    # GetClosenessCentr(G)


    # PlotClustCf(G, "example", "Directed graph - clustering coefficient")
    # PlotOutDegDistr(G, "example", "Undirected graph - out-degree Distribution")




