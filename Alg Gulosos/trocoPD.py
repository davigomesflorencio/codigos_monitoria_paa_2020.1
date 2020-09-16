import numpy as np

# Algoritmo com Programaçao Dinamica para o Problema de compra de licenças 

def trocoPD (N, tam,M):
    dp = np.zeros(N+1)
    i = 1
    while(i<=N):
        dp[i] = 1000000;
        for j in range(0,tam-1):
            if(i-M[j] >= 0):
                dp[i] = min(dp[i], dp[ i-M[j] ]+1)
        i+=1
    print(dp)
    return dp[N]

if __name__ == '__main__':
    N=8
    tam=3
    M=[1,4,6]
    print(trocoPD(N,tam,M))
    