from Grafo import grafo
import networkx as nx
import matplotlib.pyplot as plt

import heapq
# https://docs.python.org/2/library/heapq.html

def dijkstra(G, s):
    distances = {} 
    pais = {} 

    for node in G.getNodes():
        distances[node] = float('inf')
        pais[node] = None
    
    distances[s] = 0

    Q = []

    heapq.heappush(Q, (distances[s], s))

    while len(Q) != 0:
        ( _ , u) = heapq.heappop(Q)

        for i in G.getNeighbors(u):
            if distances[i] > distances[u] + G.graph.edges[u,i]['peso']:
                distances[i] = distances[u] + G.graph.edges[u,i]['peso']
                pais[i] = u

                heapq.heappush(Q, (distances[i], i))
        
    print("pais ",pais)
    print("distancias ",distances)
    

if __name__ == '__main__':
    g = grafo.Graph()
    g.addMultipleNodes([1,2,3,4,5,6])
    g.addEdge(1,2,1)
    g.addEdge(1,4,1)

    g.addEdge(2,4,1)
    g.addEdge(3,2,2)

    g.addEdge(3,4,1)
    g.addEdge(3,5,1)
    g.addEdge(3,6,1)

    g.addEdge(4,5,2)
    g.addEdge(4,6,15)

    g.addEdge(5,6,1)

    labelsG = {}
    for v1,v2,peso in g.graph.edges.data('peso'):
        labelsG[(v1,v2)] = peso

    pos = nx.spring_layout(g.graph)
    nx.draw(g.graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(g.graph, pos, labelsG)
    plt.show()

    dijkstra(g,1)

    