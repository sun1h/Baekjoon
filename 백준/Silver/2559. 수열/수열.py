N,K=map(int, input().split())
arr=list(map(int, input().split()))
lst=[]
lst.append(sum(arr[:K]))
for i in range(N-K):
    lst.append(lst[i]-arr[i]+arr[K+i])
print(max(lst))