C=int(input())
for tc in range(C):
    arr=list(map(int,input().split()))
    av=sum(arr[1:])/arr[0]
    tmp=0
    for i in range(1,len(arr)):
        if arr[i] > av:
            tmp+=1
    rate=tmp/arr[0]*100
    print(f'{rate:.3f}%')