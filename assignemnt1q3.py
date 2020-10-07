import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections
import time


names = ['karate','dolphins','lesmis','netscience']


for n in [names[0]]:
    #The edge list always had the left entry having node number less than the right entry

    edge_list = pd.read_csv(f"{n}.dat")
    edge_list.columns = range(len(edge_list.columns))
    edge_list.iloc[np.isnan(edge_list[1]),1] = -1
    edge_list = edge_list.astype('int')

    list_edge_list = []
    #adjacency_list = np.zeros([int(np.max(np.max(edge_list))),1])
    adjacency_list = pd.DataFrame(columns = range(1,int(np.max(np.max(edge_list)))+1)) #if i and j appear in the edge list then their respective neighbor lists ie the columns are updated with the values
    for i in edge_list.index:
        if(edge_list[0][i] != -1 and edge_list[1][i] != -1):
            adjacency_list = adjacency_list.append({edge_list[1][i] : edge_list[0][i]},ignore_index = True)
            adjacency_list = adjacency_list.append({edge_list[0][i] : edge_list[1][i]},ignore_index = True)

    #adjacency_list.loc[np.logical_not(np.isnan(adjacency_list[1])),1]
    refined_alist = []
    for i in adjacency_list.columns:
        if(np.all(np.isnan(adjacency_list[i]))):
             # The index location is the node number  - 1 thus node number = index  +1 `
            refined_alist.append([])
        else:
            refined_alist.append(adjacency_list.loc[np.logical_not(np.isnan(adjacency_list[i])),i].values)
    
    for i in range(len(refined_alist)):

        refined_alist[i] = np.sort(refined_alist[i]) # sroted the neighbors of the nodes of the adjacency list
    degree = []
    no_of_neighbors_connected = []
    for i in range(len(refined_alist)):
        degree.append(len(refined_alist[i]))
        neighbors = refined_alist[i] #each of the neighbors pairs of vertex i are considered and if they are connected that means a triangle is formed. The pairs are formed by using the sorted neighbor list (ascending order) and the jth index (larger) makes j-1 pairs with neigbors at indices less than j 
        no_of_neighbors_connected.append(0)    
        for j in range(1,degree[i]+1): # the j counter holds the index value on which the larger value is present of the two
            p = j-1                     #using p to keep indices in the list of uniform type (0 to n-1)
            for k in range(p):
                if(neighbors[p] in refined_alist[k]):
                    no_of_neighbors_connected[i] += 1
    no_of_neighbors_connected = np.array(no_of_neighbors_connected)
    degree = np.array(degree)
    no_of_pairs_of_neighbors_possible = 0.5 * degree * (degree - 1)
    global_clustering_coeff = np.divide(no_of_neighbors_connected.sum() , no_of_pairs_of_neighbors_possible.sum())
    local_clustering_coeff = np.divide(no_of_neighbors_connected , no_of_pairs_of_neighbors_possible)
    local_clustering_coeff[np.where(np.isfinite(local_clustering_coeff) == 0)] = 0
    #local_clustering_coeff = local_clustering_coeff.reshape(local_clustering_coeff.size)
    
    
                    
    
    
            
        
    

##    for i in edge_list.index:
##            list_edge_list.append((edge_list.iloc[i,0],edge_list.iloc[i,1]))
##
##    #degree from edge_list i is the node number
##
##    #(edge_list.iloc[:,0]==i).sum() + (edge_list.iloc[:,1]==2).sum()
##
##
##    X = []
##
##    Y = []
##
##    Degreeseq = []
##    for i in range(len(list_edge_list)):
##        X.append(list_edge_list[i][0])
##        Y.append(list_edge_list[i][1])
##
##    for i in range(int(np.max(np.max(edge_list))) + 1):
##        Degreeseq.append((edge_list.iloc[:,0]==i).sum() + (edge_list.iloc[:,1]==2).sum())
##
##    Degreeseq.remove(0)
##
##    degreeCount = collections.Counter(Degreeseq)
##    deg, cnt = zip(*degreeCount.items())
##
##
    lccCount = collections.Counter(local_clustering_coeff)
    lcc, count  = zip(*lccCount.items())
    count = pd.Series(count)
    lcc = pd.Series(lcc)
    lcc.sort_values(inplace= True)
    count.iloc[lcc.index]
    fig1, ax1 = plt.subplots()
    plt.scatter(np.array(range(1,int(np.max(np.max(edge_list))) + 1)), local_clustering_coeff, color="b")
    plt.title(f" {n } Local Clustering Coeff Scatter ")
    plt.ylabel("LCC")
    plt.xlabel("Nodel Lable")
    plt.show()
    fig2, ax2 = plt.subplots()
    plt.title(f" {n } Local Clustering Coeff Distribution ")
    plt.ylabel("Count")
    plt.xlabel("LCC")
    plt.plot(lcc,count)
    plt.show()
    


    


