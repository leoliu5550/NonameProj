#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/4 21:46
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : Floyd_Warshall.py
# @Statement : The Floyd-Warshall algorithm for the shortest path problem
# @Reference : Floyd R W. Algorithm 97: shortest path[J]. Communications of the ACM, 1962, 5(6): 345.


def pathfindalg(network):
    """
    The main function of the Floyd-Warshall algorithm
    :param network: {node1: {node2: length, node3: length, ...}, ...}
    :return:
    """
    # Step 1. Initialization
    nn = len(network)  # node number

    inf = float('inf')
    dis_mat = [[inf for _ in range(nn)] for _ in range(nn)]
    path_mat = [[[] for _ in range(nn)] for _ in range(nn)]
    
    for node1 in range(nn):
        dis_mat[node1][node1] = 0
        path_mat[node1][node1] = [node1]
        for node2 in network[node1].keys():
            dis_mat[node1][node2] = network[node1][node2]
            path_mat[node1][node2] = [node1, node2]
            
    # print("dis_mat")
    # for row in dis_mat:
    #     print(row)
    # print("path_mat")
    # for row in path_mat:
    #     print(row)
    # Step 2. The main loop:
    for k in range(nn):
        for i in range(nn):
            for j in range(nn):
                if dis_mat[i][j] > dis_mat[i][k] + dis_mat[k][j]:
                    dis_mat[i][j] = dis_mat[i][k] + dis_mat[k][j] #error  dis_mat[k][i]
                    path_mat[i][j] = path_mat[i][k].copy()
                    path_mat[i][j].pop()
                    path_mat[i][j].extend(path_mat[k][j])
                    
    return {'path': path_mat, 'length': dis_mat}


def trans_strmap(network):
    def stringNode_mapping(network):
        mapping_dict ={}
        for i,key in enumerate(network.keys()):
            mapping_dict[key] = i
        return mapping_dict
    
    mapping = stringNode_mapping(network)

    updated_network = {}
    for key,value_dict in network.items():
        subdict = {}
        for sub_key,sub_value in value_dict.items():
            subdict[mapping[sub_key]] = sub_value
        updated_network[mapping[key]] = subdict
    reversed_mapping = {}
    
    for key,val in mapping.items():
        reversed_mapping[val] = key
    return updated_network,reversed_mapping,mapping