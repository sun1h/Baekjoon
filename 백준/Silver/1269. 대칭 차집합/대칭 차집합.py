
A, B = map(int,input().split())
lsta=list(map(int,input().split()))
lstb=list(map(int,input().split()))
l=list(set(lsta)^set(lstb))
print(len(l))