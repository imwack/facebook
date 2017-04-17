#coding=utf-8
import snap

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

    #Save as Graph
    FOut = snap.TFOut("./facebook_combined/facebook.graph")
    G.Save(FOut)
    FOut.Flush()
