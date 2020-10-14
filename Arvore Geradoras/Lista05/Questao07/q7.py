from Fila1 import fila
import grafo
from collections import defaultdict

BRANCO = 0
CINZA = 1
PRETO = 2


def bfs(G, r):
    cor = defaultdict(list)
    for no in G.getNodes():
        cor[no] = BRANCO

    cor[r] = CINZA
    # print("lista ", lista)
    Q = fila.Fila()

    Q.insere(r)

    while True:
        for i in G.getNeighbors(r):
            if(cor[i] == BRANCO):
                cor[i] = CINZA
                Q.insere(i)
        cor[r] = PRETO
        if(Q.primeiro != None):
            r = Q.remove().dado
            # print("dado", r)
        else:
            print("comeco", r)
            bfs_2(G, r)
            break


def bfs_2(G, r):
    cor = defaultdict(list)
    distancia = defaultdict(list)
    for no in G.getNodes():
        cor[no] = BRANCO
        distancia[no] = 0

    cor[r] = CINZA
    distancia[r] = 0
    # print("lista ", lista)
    Q = fila.Fila()

    Q.insere(r)
    h = 0
    while True:
        for i in G.getNeighbors(r):
            if(cor[i] == BRANCO):
                cor[i] = CINZA
                distancia[i] = distancia[r]+1
                Q.insere(i)
        cor[r] = PRETO
        if(Q.primeiro != None):
            r = Q.remove().dado
            # print("dado", r)
        else:
            print("fim", r)
            print("diametro ", distancia[r])
            break


if __name__ == '__main__':
    g = grafo.Graph()
    g.addMultipleNodes(['a', 'b', 'c', 'd', 'e'])
    g.addEdge('a', 'b')
    g.addEdge('a', 'c')
    g.addEdge('a', 'd')
    g.addEdge('b', 'e')
    bfs(g, 'b')


#    print(g.getNodes())
