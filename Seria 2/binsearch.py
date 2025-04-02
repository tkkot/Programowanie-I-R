def bin_search(N, L, min, max):     #TODO: Dodać edge-case'y (idiotproofing)
    if(min>=max):
        return max if L[max]==N else -1
    m=(min+max)//2
    if N<=L[m]:
        return bin_search(N,L,min,m)
    else:
        return bin_search(N,L,m+1,max)

n=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(bin_search(n, l, 0, len(l)-1))