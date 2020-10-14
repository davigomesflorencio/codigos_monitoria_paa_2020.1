#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np

def Prim(G = nx.Graph(), R = None):
    Q    = {}
    pred = {}
    
    for v,data in G.nodes(data=True):
        Q[v]    = np.inf
        pred[v] = 'null'

    # Inicializamos a raiz da árvore com valor 0, e criamos uma árvore chamada
    # MST apenas com os vértices de G.
    Q[R] = 0.0
    MST  = nx.create_empty_copy(G)

    while Q:
        u = min(Q,key=Q.get)

        del Q[u]
        
        for vizinho in G[u]:
            if vizinho in Q:
                if G[u][vizinho]['weight'] < Q[vizinho]:
                    pred[vizinho] = u
                    Q[vizinho]    = G[u][vizinho]['weight']
      
        if pred[u] is not 'null':
            for v1,v2,data in G.edges.data('weight'):
                # para preservar os dados da aresta, foi necessário esse loop
                # que verifica todas as arestas do grafo e procura a aresta
                # (pred(u),u), porém, como um grafo não direcionado da
                # biblioteca não duplica a existência de suas arestas no
                # conjunto de arestas, isto é, se tem (u,v) não tem (v,u), há a
                # necessidade de verificar, no caso de grafos não direcionados,
                # se há a existência da aresta (u,pred(u)) ao invés de
                # (pred(u),u)
                if ( v1 is pred[u] and v2 is u ):
                    MST.add_edge(pred[u],u,weight=data)
                elif (  ( v1 is u and v2 is pred[u] ) and   ( not nx.is_directed(G) )  ):
                    MST.add_edge(pred[u],u,weight=data)
    return MST
