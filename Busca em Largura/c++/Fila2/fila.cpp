#include <iostream>
#include <queue>

using namespace std;

class Fila {
	private:
    deque<int> fila;

	public:
	Fila(){
	}

	void Enqueue(int valor)
    {
        fila.push_back(valor);
    }

    void Print()
    {
        deque<int>::iterator it = fila.begin();
        cout << "\nMostrando os elementos da fila: ";
        it = fila.begin();
        while(it != fila.end())
            cout << *it++ << " ";
    }

    void Dequeue()
    {
        if(!fila.empty()){
            fila.pop_front();
        }else{
            cout<<"Não foi possivel remover pois a lista está vazia";
        }
    }	
};
