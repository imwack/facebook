#coding=utf-8
import snap
import os
from random import randint
from egoFeatureExtract import extractFeature
from egoFeatureExtract import extractGraphFeature


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

# 加载无向图
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

# 加载有向图
def loadDGraph(path, numberOfNodes):
    G = snap.TNGraph.New()  # create undirected graph
    NodeId = []
    f = open(path, 'r')
    for line in f.readlines():
        nodes = line.split('\t')
        n1 = int(nodes[0])
        n2 = int(nodes[1])
        if not G.IsNode(n1):
            G.AddNode(n1)
            NodeId.append(n1)
        if not G.IsNode(n2):
            G.AddNode(n2)
            NodeId.append(n2)
        G.AddEdge(n1, n2)
    f.close()
    return G,NodeId


def injectNodeWithId(number, dest_num, G, path, NodeId):
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
        anomaly_node.append(NodeId[source])
        #G.AddNode(i+n)
        for i in range(0, dest_num):
            dest = randint(0, n-1)
            G.AddEdge(NodeId[source], NodeId[dest])
    path = ".//graph//"+path+str(number)+"_anomaly"
    f = open(path,'w')
    for node in anomaly_node:
        f.write(str(node)+"\n")
    f.close()
    return anomaly_node

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

def WriteFeature(features, anomaly_node, featureFile, labelFile, G, id=False):
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
    if id:
        for NI in G.Nodes():
            id = NI.GetId()
            if id in anomaly_node:
                lfile.write("1\n")
            else:
                lfile.write("0\n")
    else:
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
    G,NodeId = loadDGraph(path, numberOfNodes) #
    # 随机生成图

    # 注入节点 写入anomaly文件
    numberOfAnomaly = 400
    numberOfDest = 20
    print G.GetEdges(),G.GetNodes()
    # anomaly_node = injectNode(numberOfAnomaly, numberOfDest, G, filename)
    anomaly_node = injectNodeWithId(numberOfAnomaly, numberOfDest, G, filename, NodeId)
    print "After inject:",G.GetEdges(),G.GetNodes()

    # 写入文件.graph 方便下次读取
    graphPath = ".//graph//"+filename+str(numberOfAnomaly)+".graph"
    print "Save graph:", graphPath
    FOut = snap.TFOut(graphPath)
    G.Save(FOut)
    FOut.Flush()

    # 提取特征
    print "Begin extract feature..."
    # feature = extractFeature(G)
    feature = extractGraphFeature(G)

    # 写入特征文件
    featureFile = ".\\feature\\"+filename+str(numberOfAnomaly)
    labelFile = ".\\feature\\"+filename+str(numberOfAnomaly)+"label"
    WriteFeature(feature, anomaly_node, featureFile, labelFile, G, id=True)

    # GetNodeDegree(G)
    # GetPageRank(G)
    # GetHits(G)
    # GetDegreeCentr(G)
    # GetBetweennessCentr(G)
    # GetClosenessCentr(G)
