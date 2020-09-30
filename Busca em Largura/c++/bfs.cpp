#include <iostream>
#include <queue>
#include "Grafo/grafo.cpp"

void bfs(Grafo grafo,int v)
{
	
}

int main(int argc, char const *argv[])
{
    int V = 8;

	Grafo grafo(V);

	grafo.adicionarAresta(0, 1);
	grafo.adicionarAresta(0, 2);
	grafo.adicionarAresta(1, 3);
	grafo.adicionarAresta(1, 4);
	grafo.adicionarAresta(2, 5);
	grafo.adicionarAresta(2, 6);
	grafo.adicionarAresta(6, 7);

	bfs(grafo,1);

    return 0;
}
