N=int(input())
tmp=0
arr=[]
last=0
i=N
while i >=0:
    lst=[N,i]
    j=0
    i -= 1
    while lst[j]-lst[j+1]>=0:
        last=lst[j]-lst[j+1]
        j+=1
        lst.append(last)
        if tmp < len(lst):
            tmp=len(lst)
            arr=lst

print(len(arr))
print(*arr)