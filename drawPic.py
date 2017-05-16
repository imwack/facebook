#coding=utf-8
from snap import *
from featureExtract import *
import matplotlib.pyplot as plt
from pltUtil import *


if __name__ == '__main__':
    FIn = snap.TFIn("./facebook_combined/artificial.graph")
    G = snap.TNGraph.Load(FIn)

    degree_number = GetDegree(G)       #degree-number dic
    plotDegree(degree_number)

    # PlotClustCf(G, "example", "Directed graph - clustering coefficient")
    # PlotOutDegDistr(G, "example", "Undirected graph - out-degree Distribution")




