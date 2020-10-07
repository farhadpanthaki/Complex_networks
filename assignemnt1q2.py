import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections
import time


names = ['celegansneural','pgp-strong-2009']


for n in names:
    #The edge list always had the left entry having node number less than the right entry

    edge_list = pd.read_csv(f"{n}.dat")
    edge_list.columns = range(len(edge_list.columns))
    #NaN handling using np.nan, replace the NaN with -1 This means that the 
   #edge_list.index[np.isnan(edge_list[1])]
    edge_list.iloc[edge_list.index[np.isnan(edge_list[1])],1] = -1
    edge_list = edge_list.astype('int')

    list_edge_list = []

    for i in edge_list.index:
            list_edge_list.append((edge_list.iloc[i,0],edge_list.iloc[i,1]))

    #degree from edge_list i is the node number

    #(edge_list.iloc[:,0]==i).sum() + (edge_list.iloc[:,1]==2).sum()


    #X = []

    #Y = []

    INDegreeseq = []
    OUTDegreeseq = []
   # for i in range(len(list_edge_list)):
    #    X.append(list_edge_list[i][0])
     #   Y.append(list_edge_list[i][1])

    for i in range(int(np.max(np.max(edge_list))) + 1):
        
        indegloc = edge_list.index[edge_list.iloc[:,0]==i]# contains the locations where the ith node is the end node for an edge
        #outdegloc = edge_list.index[edge_list.iloc[:,1]==i]
        INDegreeseq.append((edge_list.iloc[:,0]==i).sum() - (edge_list.iloc[indegloc,1] == -1).sum())  # For each node i we calculate the number of times it is the end node of the directed edge
        OUTDegreeseq.append((edge_list.iloc[:,1]==i).sum())
          
        
    INDegreeseq.pop(0)
    OUTDegreeseq.pop(0)
    
    INdegreeCount = collections.Counter(INDegreeseq)
    OUTdegreeCount = collections.Counter(OUTDegreeseq)
    INdeg, INcnt = zip(*INdegreeCount.items())
    OUTdeg, OUTcnt = zip(*OUTdegreeCount.items())
    
    



    fig1, ax1 = plt.subplots()
   # fig1, ax2 = plt.subplots()
    
    plt.bar(INdeg, INcnt, width=0.80, color="b")
    

    plt.title(f" {n } INDegree Histogram ")
    plt.ylabel("Count")
    plt.xlabel("Degree")
  
    plt.show()

    plt.bar(OUTdeg, OUTcnt, width=0.80, color="b")
    plt.title(f" {n } OUTDegree Histogram ")
    plt.ylabel("Count")
    plt.xlabel("Degree")

    plt.show()
    


    


