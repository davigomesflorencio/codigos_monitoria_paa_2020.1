#include "heap.h"


void inicializarHeap(Heap * h, int tamanhoMax){
	h->V = malloc(sizeof(Vertice)*(tamanhoMax+1));
	h->tamanhoAtual = 0;
	h->tamanhoMaximo = tamanhoMax;
}

void destruirHeap(Heap * h){
	int tamanho = h->tamanhoMaximo;
	free(h->V);
	h->tamanhoMaximo = 0;
	h->tamanhoAtual = 0;
}

int pai(int i){
	return i/2;
}

int filhoEsquerda(int i){
	return 2*i;
}

int filhoDireita(int i){
	return 2*i + 1;
}

// Insere no final do arranjo do heap
bool inserirForaDeOrdem(Heap * h, Vertice vert){
	if (h->tamanhoAtual < h->tamanhoMaximo){
		(h->tamanhoAtual)++;
		h->V[h->tamanhoAtual] = vert;
		return true;
	}
	return false;
}

// Insere no final do arranjo do heap, depois verifica se está na posicão correta, colocando na ordem do Heap
bool inserirHeap(Heap * h, Vertice vert){
	int i;
	Vertice temp;
	if (h->tamanhoAtual == h->tamanhoMaximo) return false;
	(h->tamanhoAtual)++;
	i = h->tamanhoAtual;
	h->V[i] = vert;
	while ((i>1) && (h->V[pai(i)].d > h->V[i].d)){
		temp = h->V[i];
		h->V[i] = h->V[pai(i)];
		h->V[pai(i)] = temp;       
		i = pai(i);
	}
	return true;
}

// Imprime o arranjo (na ordem que estiver)
void imprimirArranjo(Heap h){
	int tamanho = h.tamanhoAtual;
	int i;
	Vertice vert;
	for (i=1;i<=tamanho;i++){
		vert = h.V[i];
		printf("%d %d\n",vert.x, vert.y);
	}
	printf("\n");
}

// Método auxiliar que pressupoe que o heap para qualquer j>i estah ordenado
// porem o elemento i nao eh necessariamente menor que seus filhos           
void minHeapify(Heap * h, int i){
	int esq = filhoEsquerda(i);
	int dir = filhoDireita(i);
	Vertice temp;
	int menor = i;
	
	//Compara se os filhos são menores que o pai
	if ((esq <= h->tamanhoAtual) && (h->V[esq].d < h->V[menor].d)) menor = esq;
	if ((dir <= h->tamanhoAtual) && (h->V[dir].d < h->V[menor].d)) menor = dir;
	
	//Se encontrou menor diferente do atual, realiza a troca
	if (menor != i) {
		temp = h->V[i];
		h->V[i] = h->V[menor];
		h->V[menor] = temp;
		minHeapify(h, menor);
	}
}

// Constroi heap a partir do arranjo usando o metodo minHeapify
void construirHeapMinimo(Heap * h){
	int metadeTamanho = h->tamanhoAtual/2;
	for (int i = metadeTamanho; i>0; i--) 
		minHeapify(h,i);
}

// Imprime elementos em ordem crescente e esvazia o heap
void heapSort(Heap * h){
	int tamanho = h->tamanhoAtual;
	int i;
	Vertice temp;
	construirHeapMinimo(h);  // Se o arranjo jah for um heap, nao precisa desta linha
	//Troca o último node pela raiz, remove a raiz que agora está na posição do ultimo node, e ordena o Heap novamente
	for (i = tamanho; i>1; i--){
		temp = h->V[1];
		h->V[1] = h->V[i];
		h->V[i] = temp;
		printf("%d ", temp.d);
		(h->tamanhoAtual)--;
		minHeapify(h, 1);
	}
	//printf("\n");
	h->tamanhoAtual = tamanho;
}

// Extrai o elemento mínimo (baseado no método heapSort). Extrai o elemento mínimo, e remove ele do heap.
Vertice extrairMin(Heap * h){
	int tamanho = h->tamanhoAtual;
	int i;
	Vertice min;
	construirHeapMinimo(h);  // Certificar que está ordenado

	//Troca o último node pela raiz, remove a raiz que agora está na posição do ultimo node, e ordena o Heap novamente
	min = h->V[1];
	h->V[1] = h->V[tamanho];
	h->V[tamanho] = min;
	//printf("%d %d",min.x, min.y);
	(h->tamanhoAtual)--;
	minHeapify(h,1);

	//printf("\n");
	return min;
}