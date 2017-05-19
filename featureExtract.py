#coding=utf-8
import snap
import os
from random import randint
from egoFeatureExtract import extractFeature

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


# 无向图
def ExtractFeature(UGraph):
    path = os.getcwd() + "\\feature\\feature.txt"
    f = open(path, 'w')

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

        f.write(str(NI.GetDeg())+"\t"+str(PRankH[id])+"\t"+str(DegCentr)+"\t"+
                str(NIdHubH[id])+"\t"+str(NIdAuthH[id])+"\t"+str(CloseCentr)+"\t" + str(Nodes[id])+"\n")

    f.close()

# 有向图
def ExtractFeatureGraph(Graph):
    path = os.getcwd() + "\\feature\\feature.txt"
    f = open(path, 'w')

    print "Get PageRank..."
    PRankH = snap.TIntFltH()
    snap.GetPageRank(Graph, PRankH)

    print "Get Hits..."
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(Graph, NIdHubH, NIdAuthH)

    print "GetBetweenness..."
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)

    print "Write File..."
    for NI in Graph.Nodes():
        id = NI.GetId()
        CloseCentr = snap.GetClosenessCentr(Graph, NI.GetId())

        #print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
        #   degree PRankH  DegCentr NIdHubH NIdAuthH   CloseCentr  GetBetweennessCentr

        f.write(str(NI.GetInDeg())+"\t"+str(NI.GetOutDeg())+"\t"+str(PRankH[id])+"\t"+
                str(NIdHubH[id])+"\t"+str(NIdAuthH[id])+"\t"+str(CloseCentr)+"\t" + str(Nodes[id])+"\n")

    f.close()


def ExtractLabel(G):
    '''
    :param G:图 
    :param number: 注入结点数目 
    :return: 
    '''
    anomaly_node = []
    with open("./facebook_combined/anomaly",'r') as ff:
        for line in ff:
            anomaly_node.append(int(line.strip()))
    ff.close()
    print anomaly_node

    path = os.getcwd() + "\\feature\\label.txt"
    f = open(path, 'w')
    n = G.GetNodes()
    for i in range(0,n):
        if(i not in anomaly_node):
            f.write("0"+"\n")
        else:
            f.write("1"+"\n")

    f.close()

def FeatureExtract():
    # FIn = snap.TFIn("./facebook_combined/facebook.graph")
    # G = snap.TUNGraph.Load(FIn)
    G = snap.GenRndGnm(snap.PNGraph, 10000, 100000)
    print G.GetNodes()
    print G.GetEdges()  #Total Edges
    anomaly_node = injectNode(1000, 20, G)   # 注入异常结点
    # ExtractFeature(G)  # 提取特征
    ExtractFeatureGraph(G)  # 提取特征
    ExtractLabel(G)  # 提取分类
    return G

def loadUNGraph(path, numberOfNodes):
    G = snap.TNGraph.New()  # create undirected graph
    for i in range(0, numberOfNodes):  # Nodes	4039
        G.AddNode(i)
    f = open(path, 'r')
    for line in f.readlines():
        nodes = line.split(' ')
        G.AddEdge(int(nodes[0]), int(nodes[1]))
    f.close()
    return G

def loadDGraph(path, numberOfNodes):
    G = snap.TUNGraph.New()  # create undirected graph
    for i in range(0, numberOfNodes):  # Nodes	4039
        G.AddNode(i)
    f = open(path, 'r')
    for line in f.readlines():
        nodes = line.split('\t')
        G.AddEdge(int(nodes[0]), int(nodes[1]))
    f.close()
    return G


def injectNode(number, dest_num, G, path):
    '''
    :param number: 异常节点数目 
    :param dest_num: 目的节点数目
    :param G: 图
    :return: 图
    '''
    n = G.GetNodes()
    anomaly_node = []

    #print dest_node
    for i in range(0, number):
        source = randint(0, n-1)
        anomaly_node.append(source)
        #G.AddNode(i+n)
        for i in range(0, dest_num):
            dest = randint(0, n-1)
            G.AddEdge(source, dest)
    path = ".//graph//"+path+str(number)+"_anomaly"
    f = open(path,'w')
    for node in anomaly_node:
        f.write(str(node)+"\n")
    f.close()
    return anomaly_node

def WriteFeature(features, anomaly_node, featureFile, labelFile):
    print "Writ Feature File:",featureFile
    n = len(features)
    ffile = open(featureFile,'w')
    for feature in features:
        for feat in feature:
            ffile.write(str(feat)+"\t")
        ffile.write("\n")
    ffile.close()

    print "Write Label File:",labelFile
    lfile = open(labelFile,'w')
    for i in range(n):
        if(i in anomaly_node):
            lfile.write("1\n")
        else:
            lfile.write("0\n")
    lfile.close()

if __name__ == '__main__':
    # 读取图
    filename = "Wiki-Vote"
    numberOfNodes = 7115    #facebook 4039
    path = os.getcwd() + "\\graph\\" + filename
    # G = loadUNGraph(path, numberOfNodes)
    G = loadDGraph(path, numberOfNodes) #
    # 随机生成图

    # 注入节点 写入anomaly文件
    numberOfAnomaly = 400
    numberOfDest = 20
    print G.GetEdges()
    anomaly_node = injectNode(numberOfAnomaly, numberOfDest, G, filename)
    print "After inject:",G.GetEdges()

    # 写入文件.graph 方便下次读取
    graphPath = ".//graph//"+filename+str(numberOfAnomaly)+".graph"
    print "Save graph:", graphPath
    FOut = snap.TFOut(graphPath)
    G.Save(FOut)
    FOut.Flush()

    # 提取特征
    print "Begin extract feature..."
    feature = extractFeature(G)

    # 写入特征文件
    featureFile = ".\\feature\\"+filename+str(numberOfAnomaly)
    labelFile = ".\\feature\\"+filename+str(numberOfAnomaly)+"label"
    WriteFeature(feature, anomaly_node, featureFile, labelFile)

    # GetNodeDegree(G)
    # GetPageRank(G)
    # GetHits(G)
    # GetDegreeCentr(G)
    # GetBetweennessCentr(G)
    # GetClosenessCentr(G)
