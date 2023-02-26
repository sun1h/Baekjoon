N=int(input())
arr=list(map(int,input().split()))
dp_in=[1 for _ in range(N)]
dp_de=[1 for _ in range(N)]

for i in range(1,len(arr)):
    if arr[i-1] <= arr[i]:
        dp_in[i]=dp_in[i-1]+1
    if arr[i-1] >= arr[i]:
        dp_de[i]=dp_de[i-1]+1

if max(dp_in)>=max(dp_de):
    print(max(dp_in))
else:
    print(max(dp_de))