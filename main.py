#coding=utf-8
from snap import *
from featureExtract import *
import matplotlib.pyplot as plt
from pltUtil import *


if __name__ == '__main__':
    FIn = snap.TFIn("./facebook_combined/facebook.graph")
    G = snap.TUNGraph.Load(FIn)
    #print G.GetEdges()  #Total Edges

    #degree_number = GetDegree(G)       #degree-number dic
    #plotDegree(degree_number)
    #ExtractNodeDegree(G)
    PlotClustCf(G, "example", "Directed graph - clustering coefficient")
    #PlotOutDegDistr(G, "example", "Undirected graph - out-degree Distribution")



