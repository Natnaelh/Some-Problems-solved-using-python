b={}
def makeChange(n,L):
    if n in b:
        return b[n]
    if n<0:
        return float('inf')
    if n==0:
        return 0
    s=float('inf')
    for i in range(1,len(L)+1):
        s=min(s,1+makeChange(n-L[i-1],L))
    b[n]=s
    return s
print(makeChange(14,[1,5,10,25,50,100]))
