#coding=utf-8
import snap
from random import randint

def injectNode(number, dest_num, G):
    '''
    
    :param number: 异常节点数目 
    :param dest_num: 目的节点数目
    :param G: 图
    :return: 
    '''
    n = G.GetNodes()
    dest_node = []
    for i in range(0, dest_num):
        dest = randint(0, n)
        dest_node.append(dest)
    #print dest_node
    for i in range(0, number):
        G.AddNode(i+n)
        for node in dest_node:
            G.AddEdge(i+n, node)


if __name__ == '__main__':
    G = snap.TUNGraph.New()  ##create undirected graph
    #Nodes	4039
    for i in range(0,4039):
        G.AddNode(i)
    #print G.GetNodes()  #Total Nodes

    f = open("./facebook_combined/facebook_combined.txt")
    for line in f.readlines():
        nodes = line.split(' ')
        G.AddEdge(int(nodes[0]),int(nodes[1]))
    #print G.GetEdges()  #Total Edges
    f.close()

    injectNode(40, 20, G)   # 注入异常结点
    print G.GetEdges()  # Total Edges
    print G.GetNodes()  # Total Nodes

    #Save as Graph
    FOut = snap.TFOut("./facebook_combined/facebook.graph")
    G.Save(FOut)
    FOut.Flush()
