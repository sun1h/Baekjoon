N=int(input())
total=0
for _ in range(N):
    arr=input()
    lst=[]
    for i in range(len(arr)):
        if arr[i] not in lst or arr[i]==lst[-1]:
            tmp=True
            lst.append(arr[i])
        else:
            tmp=False
            break
    if tmp==True:
        total+=1
print(total)