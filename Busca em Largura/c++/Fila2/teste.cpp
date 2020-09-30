#include "fila.cpp"

int main(int argc, char const *argv[])
{
    Fila fila;
    fila.Enqueue(3);
    fila.Enqueue(5);
    fila.Enqueue(7);
    fila.Enqueue(1);
    fila.Print();
    cout <<"\nDesenfileira";
    fila.Dequeue();
    cout <<"\nDesenfileira\n";
    fila.Dequeue();
    fila.Print();
    cout<<"\n";
    return 0;
}



