h,v=map(int,input().split())
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
lst_h=[0,h]
lst_v=[0,v]
for i in range(len(arr)):
    if arr[i][0]==0:
        lst_v.append(arr[i][1])
    elif arr[i][0]==1:
        lst_h.append(arr[i][1])
lst_h.sort()
lst_v.sort()
di_h=[]
di_v=[]
for i in range(len(lst_h)-1):
    di_h.append(lst_h[i+1]-lst_h[i])
for i in range(len(lst_v)-1):
    di_v.append(lst_v[i+1]-lst_v[i])
di_h.sort()
di_v.sort()
print(di_h[-1]*di_v[-1])
