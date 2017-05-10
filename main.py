#coding=utf-8
import snap
from featureExtract import *
import matplotlib.pyplot as plt
from pltUtil import *


if __name__ == '__main__':
    FIn = snap.TFIn("./facebook_combined/facebook.graph")
    G = snap.TUNGraph.Load(FIn)
    #print G.GetEdges()  #Total Edges
    degree_number = GetDegree(G)
    plotDegree(degree_number)


