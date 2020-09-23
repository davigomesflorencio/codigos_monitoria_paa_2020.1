class Frac:
    def __init__(self,vi,pi,i):
        self.vi=vi
        self.pi=pi
        self.ind=i
        self.frac=vi/pi

    def __gt__(self, other):
        return (self.frac) > (other.frac)
    
    def __lt__(self, other):
        return (self.frac) < (other.frac)
    
    def __eq__(self, other):
        return (self.frac) == (other.frac)
    
    def __le__(self, other):
        return (self.frac) <= (other.frac)
    
    def __ge__(self, other):
        return (self.frac) >= (other.frac)

def Mochila_fracionaria(v,p,w):
    tot=0
    F=[]
    for i in range(len(v)):
        F.append(Frac(v[i],p[i],i))
    
    F.sort(reverse=True)

    for i in range(len(v)):
        if F[i].pi<=w:
            w-=F[i].pi
            tot+=F[i].vi
        else:
            frac=w/F[i].pi
            tot+=frac*F[i].vi
            w-=F[i].pi*frac
    return tot

if __name__ == '__main__':
    P = [10, 20, 20, 30, 40]
    V = [100, 300, 400, 600, 840]
    W = 50
    print(Mochila_fracionaria(V,P,W))
    
        
        
