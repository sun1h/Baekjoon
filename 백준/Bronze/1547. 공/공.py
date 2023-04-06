M=int(input())
lst=[i+1 for i in range(3)]
for _ in range(M):
    num1,num2=map(int,input().split())
    for l in lst:
        if num1==l:
            a=lst.index(l)
        if num2==l:
            b=lst.index(l)
    lst[a],lst[b]=lst[b],lst[a]
print(lst[0])