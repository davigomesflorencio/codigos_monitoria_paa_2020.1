#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 0

typedef int bool;

typedef struct {
	int x,y;			//Coordenadas x e y
	int d;				//Distância
	int xPai, yPai;		//Coordenadas x e y do pai
} Vertice;

typedef struct {
  Vertice *V;
  int tamanhoAtual;
  int tamanhoMaximo;
} Heap;

void inicializarHeap(Heap * h, int tamanhoMax);
void destruirHeap(Heap * h);

int pai(int i);
int filhoEsquerda(int i);
int filhoDireita(int i);

bool inserirForaDeOrdem(Heap * h, Vertice vert);
bool inserirHeap(Heap * h, Vertice vert);
void imprimirArranjo(Heap h);

void minHeapify(Heap * h, int i);
void construirHeapMinimo(Heap * h);
void heapSort(Heap * h);
Vertice extrairMin(Heap * h);