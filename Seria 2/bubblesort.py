def bubble_sort(L):
    b=1
    while(b):
        b=0
        for i in range(len(L)-1):
            if(L[i]>L[i+1]):
                L[i],L[i+1]=L[i+1],L[i]
                b=1

l=[int(i) for i in input().split()]
bubble_sort(l)
print(l)