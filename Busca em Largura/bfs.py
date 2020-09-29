from fila import Fila
from grafo import Graph
from collections import defaultdict 

BRANCO = 0
CINZA = 1
PRETO = 2

def bfs(G,r):
    lista = defaultdict(list) 
    for v in G.getNodes():
        if v!=r:
            lista[v].append(BRANCO)
    Q= Fila()
    Q.insere(r)
    while Q.primeiro!=None:
        u = Q.remove()
        for v in G.getNeighbors(u.dado):
            if lista[v]==[BRANCO]:
                lista[v]=CINZA
                Q.insere(v)
        lista[u]=PRETO
        print(u.dado)
            
        

if __name__ == '__main__':
    g = Graph()
    g.addMultipleNodes(['a','b','c','d'])
    g.addEdge('a','b')
    g.addEdge('a','c')
    g.addEdge('a','d')
    bfs(g,'b')

    

#    print(g.getNodes())
    