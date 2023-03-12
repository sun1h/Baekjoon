def solution(s):
    C=[]
    lst=[]
    
    for st in s:
        if st not in C:
            C.append(st)
        else:
            lst.append(st)
    
    C=list(set(C))
    N=len(C)
    
    for i in range(len(C)):
        if C[i] in lst:
            C[i]=0
    N=C.count(0)
    
    for i in range(N):
        C.remove(0)
    C.sort()
    
    return(''.join(C))