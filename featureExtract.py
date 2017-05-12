#coding=utf-8
import snap
import os


def GetDegree(UGraph):
    """
    获取图 度-节点数目 
    :param UGraph: 
    :return: 
    字典{degree度:number数目}
    """
    dic = dict()
    #degree = []
    #number = []
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(UGraph, DegToCntV)
    for item in DegToCntV:
        #print "%d nodes with degree %d" % (item.GetVal2(), item.GetVal1())
        dic[item.GetVal1()] = item.GetVal2()
        #degree.append(item.GetVal1())
        #number.append(item.GetVal2())
    return dic


def GetNodeDegree(G):
    '''
    获取节点度   写入文件
    :param G: 图
    :return: 
    '''
    Nodes = G.Nodes()
    path = os.getcwd()+"\\feature\\degree.txt"
    f = open(path, 'a')
    #print path
    for node in Nodes:
        f.write(str(node.GetId())+"\t"+str(node.GetDeg())+"\n")
        #print node.GetId(),":",node.GetDeg()
    f.close()


def GetPageRank(UGraph):
    path = os.getcwd() + "\\feature\\pagerank.txt"
    f = open(path, 'a')
    PRankH = snap.TIntFltH()
    snap.GetPageRank(UGraph, PRankH)
    for item in PRankH:
       # print item, PRankH[item]
        f.write(str(item)+"\t"+str(PRankH[item])+"\n")
    f.close()


def GetHits(UGraph):

    path1 = os.getcwd() + "\\feature\\hub.txt"
    f1 = open(path1, 'a')
    path2 = os.getcwd() + "\\feature\\auth.txt"
    f2 = open(path2, 'a')

    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(UGraph, NIdHubH, NIdAuthH)
    for item in NIdHubH:
        f1.write(str(item) + "\t" + str(NIdHubH[item]) + "\n")
        #print item, NIdHubH[item]
    for item in NIdAuthH:
        f2.write(str(item) + "\t" + str(NIdAuthH[item]) + "\n")
        #print item, NIdAuthH[item]

    f1.close()
    f2.close()


def GetDegreeCentr(UGraph):
    path = os.getcwd()+"\\feature\\degreeCentr.txt"
    f = open(path, 'a')

    for NI in UGraph.Nodes():
        DegCentr = snap.GetDegreeCentr(UGraph, NI.GetId())
        #print "node: %d centrality: %f" % (NI.GetId(), DegCentr)
        f.write(str(NI.GetId()) + "\t" + str(DegCentr) + "\n")
    f.close()


def GetBetweennessCentr(UGraph):
    path = os.getcwd()+"\\feature\\betweenness.txt"
    f = open(path, 'a')
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)
    for node in Nodes:
        #print "node: %d centrality: %f" % (node, Nodes[node])
        f.write(str(node) + "\t" + str(Nodes[node]) + "\n")
    f.close


def GetClosenessCentr(UGraph):
    path = os.getcwd()+"\\feature\\closeness.txt"
    f = open(path, 'a')
    for NI in UGraph.Nodes():
        CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
        #print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
        f.write(str(NI.GetId()) + "\t" + str(CloseCentr) + "\n")
    f.close


def ExtractFeature(UGraph):
    path = os.getcwd() + "\\feature\\feature.txt"
    f = open(path, 'a')

    PRankH = snap.TIntFltH()
    snap.GetPageRank(UGraph, PRankH)

    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(UGraph, NIdHubH, NIdAuthH)

    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)

    for NI in UGraph.Nodes():
        id = NI.GetId()
        CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
        DegCentr = snap.GetDegreeCentr(UGraph, NI.GetId())

        #print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
        #   degree PRankH  DegCentr NIdHubH NIdAuthH   CloseCentr  GetBetweennessCentr

        f.write(str(id)+"\t"+str(NI.GetDeg())+"\t"+str(PRankH[id])+"\t"+str(DegCentr)+"\t"+
                str(NIdHubH[id])+"\t"+str(NIdAuthH[id])+"\t"+str(CloseCentr)+"\t" + str(Nodes[id])+"\n")

    f.close()


def ExtractLabel(G, number):
    '''
    :param G:图 
    :param number: 注入结点数目 
    :return: 
    '''
    path = os.getcwd() + "\\feature\\label.txt"
    f = open(path, 'a')
    n = G.GetNodes()
    for i in range(0,n-number):
        f.write("0"+"\n")
    for i in range(0,number):
        f.write("1"+"\n")
    f.close()