#coding=utf-8
import networkx as nx
import matplotlib.pyplot as plt                 #导入科学绘图的matplotlib包

G = nx.random_graphs.barabasi_albert_graph(1000,3)   #生成一个n=1000，m=3的BA无标度网络
degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列
print degree
x = range(len(degree))                             #生成x轴序列，从1到最大度
y = [z / float(sum(degree)) for z in degree]
plt.loglog(x,y,'.')
# plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线
plt.show()                                                          #显示图表