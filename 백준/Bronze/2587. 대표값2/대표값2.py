lst=[]
for i in range(5):
    lst.append(int(input()))
print(int(sum(lst)/len(lst)))
lst.sort()
print(lst[len(lst)//2])