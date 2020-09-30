from Fila1 import fila
from Grafo import grafo
from collections import defaultdict 

BRANCO = 0
CINZA = 1
PRETO = 2

def bfs(G,r):
    lista = defaultdict(list)
    for no in G.getNodes():
        lista[no]=BRANCO

    lista[r]=CINZA
    print("lista ",lista)
    Q = fila.Fila()
    
    Q.insere(r)

    while True:
        for i in G.getNeighbors(r):
            if(lista[i]==BRANCO):
                lista[i]=CINZA
                Q.insere(i)
        lista[r]=PRETO
        if(Q.primeiro!=None):
            r = Q.remove().dado
            print("dado",r)
        else:
            break
            
if __name__ == '__main__':
    g = grafo.Graph()
    g.addMultipleNodes(['a','b','c','d'])
    g.addEdge('a','b')
    g.addEdge('a','c')
    g.addEdge('a','d')
    bfs(g,'b')

    

#    print(g.getNodes())
    