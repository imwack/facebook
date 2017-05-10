#coding=utf-8
import snap
from featureExtract import *
import matplotlib.pyplot as plt

def plotDegree(degree_number={}):
    plt.plot(degree_number.keys(), degree_number.values())
    plt.grid(True)
    plt.show()