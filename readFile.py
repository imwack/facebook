#coding=utf-8
import snap
from random import randint

def injectNode(number, G):
    n = G.GetNodes()
    dest_node = []
    for i in range(0, number):
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

    injectNode(200,G)
    print G.GetEdges()  # Total Edges
    print G.GetNodes()  # Total Nodes

    #Save as Graph
    FOut = snap.TFOut("./facebook_combined/facebook.graph")
    G.Save(FOut)
    FOut.Flush()
