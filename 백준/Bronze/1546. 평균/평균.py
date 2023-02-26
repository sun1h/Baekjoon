N=int(input())
arr=list(map(int,input().split()))
arr.sort()
for i in range(len(arr)):
    arr[i]=arr[i]/arr[-1]*100
print(sum(arr)/len(arr))