def policiaSG(V,k):
    res=0
    i=0
    j=0
    polic = []
    ladr = []
    for ind in range(len(V)):
        if V[ind]=='P':
            polic.append(ind)
        else:
            ladr.append(ind)
    while i < len(polic) and j<len(ladr):
        if abs(polic[i]-ladr[j])<=k:
            res+=1
            i+=1
            j+=1
        elif ladr[j]>polic[i]:
            i+=1
        elif ladr[j]<polic[i]:
            j+=1
    return res

if __name__ == '__main__':
    v=['P','L','L','P','L','L','P','P','L']
    k=2
    print(policiaSG(v,k))
    
