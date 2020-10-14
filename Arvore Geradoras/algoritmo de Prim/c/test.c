#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <limits.h>
#include "heap.h"

void prim(Heap *h){

	int distEuclid;
	int tamanho = h->tamanhoMaximo;
	Vertice u, auxV[tamanho];

	h->V[0].d = 0;

	int i = 0;
	while(h->tamanhoAtual > 0){		
		u = extrairMin(h);
		auxV[i] = u;
		for(int j=0; j < tamanho; j++){	
			//Cálculo da distância euclidiana
			distEuclid = sqrt(pow(u.x - h->V[j].x, 2) + pow(u.y - h->V[j].y, 2));
			//Atualização da distância do vértice j, colocando u como pai do Vértice j
			if(distEuclid < h->V[j].d && distEuclid != 0){
				h->V[j].d = distEuclid;
				h->V[j].xPai = u.x;
				h->V[j].yPai = u.y;
			}
		}
		i++;
	}
	//Imprime o Vetor de arestas ordenadas
	i=1;
	while(i < tamanho){	
		printf("%d %d\n%d %d", auxV[i].xPai, auxV[i].yPai, auxV[i].x, auxV[i].y);
		i++;
		if(i < tamanho){
			printf("\n\n");
		}
	}
	printf("\n");
}

/*
*	Função de inicialização
*	argv[0] - Nome do arquivo atual (padrão, não precisa explicitar)
*	argv[1] - Nome do arquivo de entrada
*/
int main(int argc, char *argv[]){

	//Verifica se foi passado um nome de arquivo como parâmetro
	if(argv[1] == NULL){
		printf("\nFavor informar o nome do arquivo como primeiro argumento.\n");
		return 0;
	}
    FILE* fp;
	//Abre o arquivo que foi passado por parâmetro
	fp = fopen(argv[1],"r");
	//Verifica se foi possível abrir o arquivo
	if(fp == NULL){
		printf("\nNome do arquivo '%s' inválido.\nVerifique se o arquivo existe na mesma pasta do executável.\n", argv[1]);
		return 0;
	}
	//Recebendo a quantidade de vértices do arquivo
	int numV;
	fscanf(fp, "%d",&numV);
	//Cria o Heap de vértice
	Heap h;
	inicializarHeap(&h, numV);
	//Lê os dados do arquivo e insere no heap
	Vertice v;
	for(int i=1; i<numV+1; i++){
		fscanf(fp, "%d %d", &v.x, &v.y);
		v.d = v.xPai = v.yPai = INT_MAX; 
		inserirForaDeOrdem(&h, v);
    }
	//Fecha o arquivo
	fclose(fp);
	//Executa a Árvore Geradora Mínima Prim
	prim(&h);
    return 0;
}