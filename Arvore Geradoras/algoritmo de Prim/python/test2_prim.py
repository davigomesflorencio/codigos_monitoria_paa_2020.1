#!/usr/bin/env python
# -*- coding: utf-8 -*-
import prim as p
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('o')
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('e')
G.add_node('d')
G.add_node('t')

G.add_edge('o', 'a', weight=2)
G.add_edge('o', 'b', weight=5)
G.add_edge('o', 'c', weight=4)
G.add_edge('a', 'b', weight=2)
G.add_edge('a', 'd', weight=7)  
G.add_edge('c', 'b', weight=1)
G.add_edge('c', 'e', weight=4)
G.add_edge('b', 'e', weight=3)
G.add_edge('b', 'd', weight=4)
G.add_edge('e', 'd', weight=1)
G.add_edge('e', 't', weight=7)
G.add_edge('d', 't', weight=5)

H = p.Prim(G, 'o')

labelsG = {}
for v1,v2,data in G.edges.data('weight'):
    labelsG[(v1,v2)] = data

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, labelsG)

plt.show()

labels = {}
for v1,v2,data in H.edges.data('weight'):
    labels[(v1,v2)] = data

pos = nx.spring_layout(H)
nx.draw(H,pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos, labels)

plt.show()