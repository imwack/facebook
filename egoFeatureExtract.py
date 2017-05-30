#coding = utf-8
from snap import *
import os

# 有向图
def extractTNGraph(G):



# 无向图 Egonet feature
def extractTUNGraph(G):
    # 遍历每个节点N
    for N in G2.Nodes():
        id = N.GetId() # node id
        ArndEdges = 0
        egonet = TUNGraph.New()     # 生成新无向图
        egonet.AddNode(id)          # 添加当前id作为ego
        InNode = GetInNId(N)        # Returns ID of NodeN-th in-node (the node pointing to the current node).
        OutNode = GetOutNId(NodeN)  # Returns ID of NodeN-th out-node (the node the current node points to).

# 读取无向图
def readTUNGraphFile(path):
    FIn = snap.TFIn(path)
    G = snap.TUNGraph.Load(FIn)
    return G


if __name__ =="__main__":
    filename = "facebook1000.graph"
    path = os.getwcd() + "\\facebook_combined\\"+filename
    G = readTUNGraphFile(path)
    feature = extractTUNGraph(G)