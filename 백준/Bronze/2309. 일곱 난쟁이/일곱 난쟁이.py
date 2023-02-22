arr=[]
for i in range(9):
    arr.append(int(input()))
lst=[]
n=sum(arr)-100
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == n:
            lst.append(arr[i])
            lst.append(arr[j])
            break
    if len(lst)==2:
        break
l= sorted(list(set(arr) - set(lst)))
for i in range(len(l)):
    print(l[i])