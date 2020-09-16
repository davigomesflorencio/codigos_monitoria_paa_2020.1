# Algoritmo Guloso para o Problema de compra de licenças 
# Porem nem sempre dá otimo 

def trocoSG (N, tam,M):
    total = 0
    i=tam-1
    while(i>=0):
        aux = N/M[i] 
        N -= aux * M[i] 
        total += aux
        i-=1
    return total

if __name__ == '__main__':
    N=8
    tam=3
    M=[1,4,6]
    print(trocoSG(N,tam,M))
    