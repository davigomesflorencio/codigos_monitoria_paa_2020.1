#include "fila.cpp"

int main(int argc, char const *argv[])
{
    Fila fila(20);
    fila.Enqueue(3);
    fila.Enqueue(5);
    fila.Enqueue(7);
    fila.Enqueue(1);
    fila.Print();
    cout <<"Desenfileira\n";
    fila.Dequeue();
    cout <<"Desenfileira\n";
    fila.Dequeue();
    fila.Print();
    cout<<"\n";
    return 0;
}



