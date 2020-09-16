# Algoritmo Guloso para o Problema sequencia de jobs

class pair:
    def __init__(self,ind,ti,li):
        self.ind=ind
        self.li=li
        self.ti=ti
    
    def __gt__(self, other):
        return (self.li / self.ti) > (other.li / other.ti)
    
    def __lt__(self, other):
        return (self.li / self.ti) < (other.li / other.ti)
    
    def __eq__(self, other):
        return (self.li / self.ti) == (other.li / other.ti)
    
    def __le__(self, other):
        return (self.li / self.ti) <= (other.li / other.ti)
    
    def __ge__(self, other):
        return (self.li / self.ti) >= (other.li / other.ti)


def job_sequency(T,L,tam):
    list=[]
    for i in range(tam):
        p=pair(i+1,T[i],L[i])
        list.append(p)

    list.sort(reverse=True)

    for i in range(tam):
        print(list[i].ind)

if __name__ == '__main__':
    L=[1, 2, 3, 5, 6]
    T=[2, 4, 1, 3, 2 ]
    # 0,5 -0,5 , 3 ,1,66 - 3
    N=len(T)
    job_sequency(T,L,N)
    