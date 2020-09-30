#include <iostream>
#include <queue>
#include "Grafo/grafo.cpp"

void bfs(Grafo grafo,int v)
{
	int visitados[grafo.V];

	for (int i = 0; i < grafo.V; i++)
	{
		visitados[i]=0;
	}

	visitados[v]=1;	

	queue<int> fila;
	
	while (true)
	{
		list<int>::iterator it;
		for (it=grafo.adj[v].begin(); it!=grafo.adj[v].end(); it++)
		{
			if (visitados[*it]==0)
			{
				visitados[*it]=1;
				fila.push(*it);
			}
			
		}
		visitados[v]=2;
		cout<<"Visitando o vertice "<<v<<"\n";

		if(!fila.empty()){
			v = fila.front();
			fila.pop();
		}else{
			break;
		}
	}
	
	
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

	bfs(grafo,0);

    return 0;
}
