N=int(input())
arr=list(map(int,input().split()))
M=int(input())
arr2=list(map(int,input().split()))

dic={a:0 for a in arr2}
for a in arr:
    if a in dic:
        dic[a]+=1

for a in arr2:
    if a in dic:
        print(dic[a],end=' ')