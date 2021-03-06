#coding=utf-8
from snap import *
import os

def loadUNGraph(path):
    FIn = TFIn(path)
    G = TUNGraph.Load(FIn)
    return G


# 有向图特征提取 加上id标号
def extractFeatureWithId(UGraph):
    feature = []
    PRankH = TIntFltH()
    GetPageRank(UGraph, PRankH)
    NIdHubH = TIntFltH()
    NIdAuthH = TIntFltH()
    GetHits(UGraph, NIdHubH, NIdAuthH)
    Nodes = TIntFltH()
    Edges = TIntPrFltH()
    # GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)
    # NIdEigenH = TIntFltH()
    # GetEigenVectorCentr(UGraph, NIdEigenH)

    for NI in UGraph.Nodes():
        id = NI.GetId()  # current node id
        if(id%100==0):
            print "Extract Feature:",id
        # local feature:
        # degree/PR/DegreeCentr/ClosenessCentr/FarCentr/Hub/Auth/Centrality
        temp_feature = []
        temp_feature.append(id) # id
        temp_feature.append(NI.GetInDeg())# GetDeg
        temp_feature.append(NI.GetOutDeg())  # GetDeg
        temp_feature.append(PRankH[id]) # PRankH
        CloseCentr = GetClosenessCentr(UGraph, NI.GetId())
        temp_feature.append(CloseCentr) # CloseCentr
        FarCentr = GetFarnessCentr(UGraph, NI.GetId())
        temp_feature.append(FarCentr)   # FarCentr
        temp_feature.append(NIdHubH[id])# Hub
        temp_feature.append(NIdAuthH[id]) # Auth
        # temp_feature.append(Nodes[id])  # BetweennessCentr
        # temp_feature.append(NIdEigenH[id])  # EigenVectorCentr
        temp_feature.append(GetNodeEcc(UGraph, id, False))  # node eccentricity

        # Ego Feature
        ego = TNGraph.New()     # new egonet
        ego.AddNode(id)         # add current node
        inD = NI.GetInDeg()
        for i in range(inD):
            NbrNId = NI.GetInNId(i)         # neighbor node id
            if not ego.IsNode(NbrNId):
                ego.AddNode(NbrNId)         # add neighbor node
        outD = NI.GetOutDeg()
        for i in range(outD):
            NbrNId = NI.GetOutNId(i)         # neighbor node id
            if not ego.IsNode(NbrNId):
                ego.AddNode(NbrNId)         # add neighbor node


        ArndEdges = 0;
        for i in range(inD):
            NbrNId = NI.GetInNId(i)
            NbrNode = UGraph.GetNI(NbrNId)
            NbInD = NbrNode.GetInDeg()      # neighbor node ind
            NbOutD = NbrNode.GetOutDeg()
            for j in range(NbInD):
                NbrNbrNId = NbrNode.GetInNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1
            for j in range(NbOutD):
                NbrNbrNId = NbrNode.GetOutNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1

        for i in range(outD):
            NbrNId = NI.GetOutNId(i)
            NbrNode = UGraph.GetNI(NbrNId)
            NbInD = NbrNode.GetInDeg()  # neighbor node ind
            NbOugtD = NbrNode.GetOutDeg()      # neighbor node ind
            for j in range(NbInD):
                NbrNbrNId = NbrNode.GetInNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1
            for j in range(NbOugtD):
                NbrNbrNId = NbrNode.GetOutNId(j)
                if ego.IsNode(NbrNbrNId):  # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges + 1
        temp_feature.append(ArndEdges)      # ego out nodes
        temp_feature.append(ego.GetNodes()) # ego nodes
        temp_feature.append(ego.GetEdges()) # ego edges

        feature.append(temp_feature)
    return feature

# 有向图特征提取
def extractGraphFeature(UGraph):
    feature = []
    PRankH = TIntFltH()
    GetPageRank(UGraph, PRankH)
    NIdHubH = TIntFltH()
    NIdAuthH = TIntFltH()
    GetHits(UGraph, NIdHubH, NIdAuthH)
    Nodes = TIntFltH()
    Edges = TIntPrFltH()
    # GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)
    # NIdEigenH = TIntFltH()
    # GetEigenVectorCentr(UGraph, NIdEigenH)

    for NI in UGraph.Nodes():
        id = NI.GetId()  # current node id
        if(id%100==0):
            print "Extract Feature:",id
        # local feature:
        # degree/PR/DegreeCentr/ClosenessCentr/FarCentr/Hub/Auth/Centrality
        temp_feature = []
        temp_feature.append(NI.GetInDeg())# GetDeg
        temp_feature.append(NI.GetOutDeg())  # GetDeg
        temp_feature.append(PRankH[id]) # PRankH
        CloseCentr = GetClosenessCentr(UGraph, NI.GetId())
        temp_feature.append(CloseCentr) # CloseCentr
        FarCentr = GetFarnessCentr(UGraph, NI.GetId())
        temp_feature.append(FarCentr)   # FarCentr
        temp_feature.append(NIdHubH[id])# Hub
        temp_feature.append(NIdAuthH[id]) # Auth
        # temp_feature.append(Nodes[id])  # BetweennessCentr
        # temp_feature.append(NIdEigenH[id])  # EigenVectorCentr
        temp_feature.append(GetNodeEcc(UGraph, id, False))  # node eccentricity

        # Ego Feature
        ego = TNGraph.New()     # new egonet
        ego.AddNode(id)         # add current node
        inD = NI.GetInDeg()
        for i in range(inD):
            NbrNId = NI.GetInNId(i)         # neighbor node id
            if not ego.IsNode(NbrNId):
                ego.AddNode(NbrNId)         # add neighbor node
        outD = NI.GetOutDeg()
        for i in range(outD):
            NbrNId = NI.GetOutNId(i)         # neighbor node id
            if not ego.IsNode(NbrNId):
                ego.AddNode(NbrNId)         # add neighbor node


        ArndEdges = 0;
        for i in range(inD):
            NbrNId = NI.GetInNId(i)
            NbrNode = UGraph.GetNI(NbrNId)
            NbInD = NbrNode.GetInDeg()      # neighbor node ind
            NbOutD = NbrNode.GetOutDeg()
            for j in range(NbInD):
                NbrNbrNId = NbrNode.GetInNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1
            for j in range(NbOutD):
                NbrNbrNId = NbrNode.GetOutNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1

        for i in range(outD):
            NbrNId = NI.GetOutNId(i)
            NbrNode = UGraph.GetNI(NbrNId)
            NbInD = NbrNode.GetInDeg()  # neighbor node ind
            NbOugtD = NbrNode.GetOutDeg()      # neighbor node ind
            for j in range(NbInD):
                NbrNbrNId = NbrNode.GetInNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1
            for j in range(NbOugtD):
                NbrNbrNId = NbrNode.GetOutNId(j)
                if ego.IsNode(NbrNbrNId):  # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges + 1
        temp_feature.append(ArndEdges)      # ego out nodes
        temp_feature.append(ego.GetNodes()) # ego nodes
        temp_feature.append(ego.GetEdges()) # ego edges

        feature.append(temp_feature)
    return feature

def extractFeature(UGraph):
    feature = []
    PRankH = TIntFltH()
    GetPageRank(UGraph, PRankH)
    NIdHubH = TIntFltH()
    NIdAuthH = TIntFltH()
    GetHits(UGraph, NIdHubH, NIdAuthH)
    Nodes = TIntFltH()
    Edges = TIntPrFltH()
    GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)
    NIdEigenH = TIntFltH()
    GetEigenVectorCentr(UGraph, NIdEigenH)

    for NI in UGraph.Nodes():
        id = NI.GetId()  # current node id
        if(id%100==0):
            print "Extract Feature:",id
        # local feature:
        # degree/PR/DegreeCentr/ClosenessCentr/FarCentr/Hub/Auth/Centrality
        temp_feature = []
        temp_feature.append(NI.GetDeg())# GetDeg
        temp_feature.append(PRankH[id]) # PRankH
        DegCentr = GetDegreeCentr(UGraph, id)
        temp_feature.append(DegCentr)   # DegCentr
        CloseCentr = GetClosenessCentr(UGraph, NI.GetId())
        temp_feature.append(CloseCentr) # CloseCentr
        FarCentr = GetFarnessCentr(UGraph, NI.GetId())
        temp_feature.append(FarCentr)   # FarCentr
        temp_feature.append(NIdHubH[id])# Hub
        temp_feature.append(NIdAuthH[id]) # Auth
        temp_feature.append(Nodes[id])  # BetweennessCentr
        temp_feature.append(NIdEigenH[id])  # EigenVectorCentr
        temp_feature.append(GetNodeEcc(UGraph, id, False))  # node eccentricity

        # Ego Feature
        ego = TUNGraph.New()    # new egonet
        ego.AddNode(id)         # add current node
        inD = NI.GetInDeg()
        for i in range(inD):
            NbrNId = NI.GetInNId(i)     # neighbor node id
            if not ego.IsNode(NbrNId):
                ego.AddNode(NbrNId)         # add neighbor node

        ArndEdges = 0;
        for i in range(inD):
            NbrNId = NI.GetInNId(i)
            NbrNode = UGraph.GetNI(NbrNId)
            NbInD = NbrNode.GetInDeg()      # neighbor node ind
            for j in range(NbInD):
                NbrNbrNId = NbrNode.GetInNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1
        temp_feature.append(ArndEdges)      # ego out nodes
        temp_feature.append(ego.GetNodes()) # ego nodes
        temp_feature.append(ego.GetEdges()) # ego edges

        feature.append(temp_feature)
    return feature


def extractEgoFeature(UGraph):
    feature = []

    for NI in UGraph.Nodes():
        temp_feature = []
        id = NI.GetId()  # current node id
        print "Extract Egonet Feature:",id
        ego = TUNGraph.New()    # new egonet
        ego.AddNode(id)         # add current node
        inD = NI.GetInDeg()
        for i in range(inD):
            NbrNId = NI.GetInNId(i)     # neighbor node id
            if not ego.IsNode(NbrNId):
                ego.AddNode(NbrNId)         # add neighbor node

        ArndEdges = 0
        for i in range(inD):
            NbrNId = NI.GetInNId(i)
            NbrNode = UGraph.GetNI(NbrNId)
            NbInD = NbrNode.GetInDeg()      # neighbor node ind
            for j in range(NbInD):
                NbrNbrNId = NbrNode.GetInNId(j)
                if ego.IsNode(NbrNbrNId):   # 邻居节点的邻居在ego中 且边不存在 则添加
                    if not ego.IsEdge(NbrNId, NbrNbrNId):
                        ego.AddEdge(NbrNId, NbrNbrNId)
                else:
                    ArndEdges = ArndEdges+1
        temp_feature.append(ArndEdges)      # ego out nodes
        temp_feature.append(ego.GetNodes()) # ego nodes
        temp_feature.append(ego.GetEdges()) # ego edges

        feature.append(temp_feature)
    return feature

if __name__=="__main__":
    t1 = time.time()
    filename = "facebook.graph"
    path = os.getcwd()+"\\facebook_combined\\"+filename
    G = loadUNGraph(path)
    print G.GetNodes(),G.GetEdges()
    features = extractEgoFeature(G)
    path = os.getcwd()+"\\feature\\"+filename
    f = open(path,'w')
    for feature in features:
        for feat in feature:
            f.write(str(feat)+"\t")
        f.write("\n")
    f.close()
    t2 = time.time()
    print t1,t2,t2-t1 # 4038 nodes, 27.6970000267
if __name__ =="__main__":
    filename = "facebook1000.graph"
    path = os.getwcd() + "\\facebook_combined\\"+filename
    G = readTUNGraphFile(path)
    feature = extractTUNGraph(G)