#include <iostream>
#include <list>

using namespace std;

class Grafo
{
	public:
	int V; 
	list<int> *adj; 

public:
	Grafo(int V);
	void adicionarAresta(int v1, int v2); 
	int grauVertice(int v);
};


Grafo::Grafo(int V)
{
	this->V = V; 
	adj = new list<int>[V]; 
}

void Grafo::adicionarAresta(int v1, int v2)
{
	adj[v1].push_back(v2);
}

int Grafo::grauVertice(int v)
{
	return adj[v].size();
}