def most_frequent(L):
    if not L:
        return
    L.sort()
    L.append(None)
    p=None
    n=N=0
    m=[]
    for i in L:
        if(p==i):
            n+=1
        else:
            if n>N:
                N=n
                m.clear()
                m.append(p)
            elif n==N:
                m.append(p)
            n=1
        p=i
    return [(i,N) for i in m]

l=[int(i) for i in input().split()]
# print(l)
print(most_frequent(l))