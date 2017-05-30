#coding=utf-8
import networkx as nx
from operator import itemgetter
import matplotlib.pyplot as plt

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


def genEgonet(edges, nodes):
    G = nx.generators.barabasi_albert_graph(edges, nodes)

    node_and_degree = G.degree()
    (largest_hub, degree) = sorted(node_and_degree.items(), key=itemgetter(1))[-1]
    # Create ego graph of main hub
    hub_ego = nx.ego_graph(G, largest_hub)
    # Draw graph
    pos = nx.spring_layout(hub_ego)
    nx.draw(hub_ego, pos, node_color='b', node_size=50, with_labels=False)
    # Draw ego as large and red
    nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=300, node_color='r')
    # xmin, xmax = plt.xlim()  # return the current xlim

    plt.savefig('ego_graph.png')
    plt.show()

if __name__=="__main__":
    # exampleDiGraph()
    genEgonet(400,2)