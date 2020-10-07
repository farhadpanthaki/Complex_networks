#import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections
import time


names = ['karate','dolphins','lesmis','netscience']


for n in names:
    
    #The edge list always had the left entry having node number less than the right entry

    edge_list = pd.read_csv(f"{n}.dat")
    edge_list.columns = range(len(edge_list.columns))
    edge_list.iloc[np.isnan(edge_list[1]),1] = -1 #made the nan entry -1 as a placeholder for nan
    edge_list = edge_list.astype('int')
    start_time = time.time()

    #list_edge_list = []

    #for i in edge_list.index:
            #list_edge_list.append((edge_list.iloc[i,0],edge_list.iloc[i,1]))

    #degree from edge_list i is the node number

    #(edge_list.iloc[:,0]==i).sum() + (edge_list.iloc[:,1]==2).sum()


    #X = []

    #Y = []

    Degreeseq = [] 
    #for i in range(len(list_edge_list)):
        #X.append(list_edge_list[i][0])
        #Y.append(list_edge_list[i][1])

    for i in range(int(np.max(np.max(edge_list))) + 1):
        Degreeseq.append((edge_list.iloc[:,0]==i).sum() + (edge_list.iloc[:,1]==i).sum() - (edge_list.loc[edge_list.iloc[:,0]==i,1] == -1).sum())

    Degreeseq.remove(0) #Now Contains the degree sequence of the network with the index value being the node number - 1
    print("--- %s seconds --- to get degree sequence"% (time.time() - start_time))

    degreeCount = collections.Counter(Degreeseq)
    deg, cnt = zip(*degreeCount.items()) #not sorted



    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")

    plt.title(f" {n } Degree Histogram ")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.show()

time.sleep(10)
    


    


