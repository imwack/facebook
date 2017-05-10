#coding=utf-8
import snap

def GetDegree(UGraph):
    """
    获取图 度-节点数目
    :param UGraph: 
    :return: 
    degree度 number数目
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