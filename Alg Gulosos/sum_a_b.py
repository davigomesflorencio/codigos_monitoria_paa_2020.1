def sum_a_b(a,b):
    a.sort()
    b.sort()
    s=0
    for i in range(len(a)):
        s+=abs(a[i]-b[i])
    return s

if __name__ == '__main__':

    a=[1,2,3]
    b=[3,2,1]
    print(sum_a_b(a,b))
    