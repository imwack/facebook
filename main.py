#coding=utf-8
import snap

if __name__ == '__main__':
    FIn = snap.TFIn("./facebook_combined/facebook.graph")
    G = snap.TUNGraph.Load(FIn)
    print G.GetEdges()  #Total Edges
