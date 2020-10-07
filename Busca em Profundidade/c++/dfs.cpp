#include <iostream>
#include <queue>
#include "Grafo/grafo.cpp"

using namespace std;

void dfs_visit(Grafo grafo,int v,int* visitados){
    visitados[v]=1;
    cout<<"Visitando o vertice "<<v<<"\n";
    list<int>::iterator it;
	for (it=grafo.adj[v].begin(); it!=grafo.adj[v].end(); it++)
    {
        if (visitados[*it]==0)
        {
            dfs_visit(grafo,*it,visitados);
        }   
    }

    visitados[v]=2;
}

void dfs(Grafo grafo)
{
	int visitados[grafo.V];

	for (int i = 0; i < grafo.V; i++)
	{
		visitados[i]=0;
	}

    for (int i = 0; i < grafo.V; i++)
	{
        if (visitados[i]==0)
        {
            dfs_visit(grafo,i,visitados);
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

	dfs(grafo);
    return 0;
}
