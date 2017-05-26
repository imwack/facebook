#coding=utf-8
import networkx as nx

def GenRandGraph():
    G = nx.random_graphs.barabasi_albert_graph(1000,3)  # 生成一个n=1000，m=3的BA无标度网络
    degree =  nx.degree_histogram(G)                    # 返回图中所有节点的度分布序列
    print degree
    x = range(len(degree))                              # 生成x轴序列，从1到最大度
    y = [z / float(sum(degree)) for z in degree]
    plt.loglog(x,y,'.')
    # plt.loglog(x,y,color="blue",linewidth=2)          # 在双对数坐标轴上绘制度分布曲线
    plt.show()                                          # 显示图表
    return G

def exampleGraph():
    G = nx.Graph()  # Create an undirected graph with no nodes and no edges.
    G.add_node(1)           # add a node
    G.add_nodes_from([2,5]) # add a list of nodes
    G.add_edge(1,2)         # add edge
    G.add_edges_from([(1, 2), (1, 3)])  # adding a list of edges
    G.add_node("spam")      # adds node "spam" node can be string
    print G.number_of_nodes()
    print G.number_of_edges()
    print G.nodes()
    G.neighbors(1)          # node neighbor

def exampleDiGraph():
    DG = nx.DiGraph()        #Directed graphs
    DG.add_edge(1,2)
    DG.add_edge(3,1)
    print DG.degree(1)
    print DG.out_degree(1)
    print DG.in_degree(1)
    print DG.successors(1)
    print DG.neighbors(1)


if __name__=="__main__":
    exampleDiGraph()