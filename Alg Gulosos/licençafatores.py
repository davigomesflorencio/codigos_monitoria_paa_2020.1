# Algoritmo Guloso para o Problema de compra de licenças 

class pair:
    def __init__(self,ind,fator):
        self.ind=ind
        self.fator=fator
    
    def __gt__(self, other):
        return (self.fator) > (other.fator)
    
    def __lt__(self, other):
        return (self.fator) < (other.fator)
    
    def __eq__(self, other):
        return (self.fator) == (other.fator)
    
    def __le__(self, other):
        return (self.fator) <= (other.fator)
    
    def __ge__(self, other):
        return (self.fator) >= (other.fator)

def Ordemlicencas(R):
    if len(R)==0:
        return []
    P=[]
    for i in range(len(R)):
        par = pair(i,R[i])
        P.append(par)
    
    P.sort(reverse=True)
    T=[]

    for i in range(len(R)):
        T.append(P[i].ind+1)
    
    return T

if __name__ == '__main__':
    R=[2,4,3]

    print(Ordemlicencas(R))
    

