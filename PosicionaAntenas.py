# Algoritmo Guloso para o Problema de posicionar as antenas  

def PosicionaAntenas(D):
    if len(D)==0:
        return []
    
    D.sort()
    t=[]
    t.append(D[0]+4)
    p=0
    for j in range(1,len(D)):
        if abs(D[j]-t[p]) > 4:
            p+=1
            t.append(D[j]+4)
    return t

if __name__ == '__main__':
    D=[8,4,14,26,16]

    print(PosicionaAntenas(D))
    