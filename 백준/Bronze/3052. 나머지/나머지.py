lst=[]
for i in range(10):
    n=int(input())
    lst.append(n%42)
total=0
lst2=[]
for i in range(len(lst)):
    if lst[i] not in lst2:
        lst2.append(lst[i])
        total+=1
print(total)
    