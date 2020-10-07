#include <iostream>
#include <list>
#include <queue>
#include "Grafo/grafo.cpp"

#define INFINITO 10000000

using namespace std;

void dijkstra(Grafo grafo,int s){
    int distances[grafo.V];
    /*
        vetor de visitados serve para caso o vértice já tenha sido
        expandido (visitado), não expandir mais
    */
    int visitados[grafo.V];

    // https://www.geeksforgeeks.org/priority-queue-of-pairs-in-c-ordered-by-first/

    priority_queue < pair<int, int>,vector<pair<int, int> >, greater<pair<int, int>> > pq;
    
    for(int i = 0; i < grafo.V; i++)
    {
        distances[i] = INFINITO;
        visitados[i] = false;
    }

    distances[s] = 0;
    
    pq.push(make_pair(distances[s], s));

    while(!pq.empty())
    {
        pair<int, int> p = pq.top(); // extrai o pair do topo
        int u = p.second; // obtém o vértice do pair
        pq.pop(); // remove da fila

        // verifica se o vértice não foi expandido
        if(visitados[u] == false)
        {
            visitados[u] = true;

            list<pair<int, int> >::iterator it;

            for(it = grafo.adj[u].begin(); it != grafo.adj[u].end(); it++)
            {
                int v = it->first;
                int peso_aresta = it->second;

                if(distances[v] > (distances[u] + peso_aresta))
                {
                    distances[v] = distances[u] + peso_aresta;
                    pq.push(make_pair(distances[v], v));
                }
            }
        }
    }
    for (int i = 0; i < grafo.V; i++)
    {
        cout<<distances[i]<<" ";
    }
    
}

int main(int argc, char const *argv[])
{
    int V = 5;

	Grafo g(V);

	g.adicionarAresta(0, 1, 4);
	g.adicionarAresta(0, 2, 2);
	g.adicionarAresta(0, 3, 5);
	g.adicionarAresta(1, 4, 1);
	g.adicionarAresta(2, 1, 1);
	g.adicionarAresta(2, 3, 2);
	g.adicionarAresta(2, 4, 1);
	g.adicionarAresta(3, 4, 1);

	dijkstra(g,0);
    return 0;
}
