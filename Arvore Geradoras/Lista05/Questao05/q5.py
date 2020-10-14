import grafo
from collections import defaultdict

BRANCO = 0
CINZA = 1
PRETO = 2


def dfs(G):
    visited = defaultdict(list)
    for no in G.getNodes():
        visited[no] = BRANCO
    for no in G.getNodes():
        if visited[no] == BRANCO:
            res = dfs_visit(G, no, visited)
            if(res == True):
                return True
    return False


def dfs_visit(G, v, visited):
    visited[v] = CINZA
    # print("vértice ", v)
    for i in G.getNeighbors(v):
        if visited[i] == PRETO:
            return True
        if visited[i] == BRANCO:
            dfs_visit(G, i, visited)
    visited[v] = PRETO


if __name__ == '__main__':
    g = grafo.Graph()
    g.addMultipleNodes(['a', 'b', 'c', 'd'])
    g.addEdge('a', 'b')
    g.addEdge('a', 'c')
    g.addEdge('a', 'd')
    g.addEdge('b', 'c')
    print(dfs(g))


#    print(g.getNodes())
