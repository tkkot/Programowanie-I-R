import sys


N=int(sys.argv[1])
for K in range(N+1):
    Pi=0
    sgn=1
    for n in range(1, 2*(K+1), 2):
        Pi+=sgn/n*(4*(1/5)**n-(1/239)**n)
        sgn*=-1
    print(K, 4*Pi)