def prateleirasSG(w,n,m):
    qn=0 
    qm=0
    restante=w
    p=0
    q=0
    r=0
    # print('ola')
    while w >= m:
        p =  int(w / n) 

        r = w % n
        if r<=restante:
            qn=p
            qm=q
            restante =r
        q+=1
        w-=m
    return (qn,qm)

if __name__ == '__main__':
    print(prateleirasSG(24,3,8))
    