#include <iostream>
#include <list>
#include <queue>

#define INFINITO 10000000

using namespace std;

class Grafo
{
	public:
	int V; 
	list<pair<int, int>> *adj; 

	public:
	Grafo(int V);
	void adicionarAresta(int v1, int v2,int peso); 
	int grauVertice(int v);
};


Grafo::Grafo(int V)
{
	this->V = V; 
	adj = new list<pair<int, int> >[V];
}

void Grafo::adicionarAresta(int v1, int v2,int custo)
{
	adj[v1].push_back(make_pair(v2, custo));
	// adj[v2].push_back(v1);
}

int Grafo::grauVertice(int v)
{
	return adj[v].size();
}