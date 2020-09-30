#include <iostream>
#include <queue>

using namespace std;

class Fila {
	private:
	    int ini = 0;
        int fim = 0;
        int *item;

	public:
	Fila(int tam){
	    item = (int *)malloc(sizeof(int)*tam);
	}

	 void Enqueue(int valor)
    {
        item[fim++] = valor;
    }
    int front(){
        return item[ini]; 
    }

    void Print()
    {
        for(int i = ini; i<fim; i++)
        {
            cout << item[i] <<"\n";
        }
    }

    int Dequeue()
    {
        return item[ini++];
    }	
};
