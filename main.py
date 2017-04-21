#coding=utf-8
import snap

def GetDegree(UGraph):
    """
    获取图 度-节点数目
    :param UGraph: 
    :return: 
    """
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(UGraph, DegToCntV)
    for item in DegToCntV:
        print "%d nodes with degree %d" % (item.GetVal2(), item.GetVal1())

if __name__ == '__main__':
    FIn = snap.TFIn("./facebook_combined/facebook.graph")
    G = snap.TUNGraph.Load(FIn)
    #print G.GetEdges()  #Total Edges
    GetDegree(G)
