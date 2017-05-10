#coding=utf-8
import snap
import os

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



def ExtractNodeDegree(G):
    '''
    获取节点度   写入文件
    :param G: 图
    :return: 
    '''
    Nodes = G.Nodes()
    path = os.getcwd()+"\\feature\\degree.txt"
    f = open(path,'a')
    print path
    for node in Nodes:
        f.write(str(node.GetId())+"\t"+str(node.GetDeg())+"\n")
        #print node.GetId(),":",node.GetDeg()
    f.close()




