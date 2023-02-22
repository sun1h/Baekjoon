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
p1,p2,p3,p4=0,0,0,0
len_h=0
len_v=0
for i in range(len(lst_h)-1):
    if len_h < lst_h[i+1]-lst_h[i]:
        len_h = lst_h[i+1]-lst_h[i]
        p1=lst_h[i]
        p2=lst_h[i+1]
for i in range(len(lst_v)-1):
    if len_v < lst_v[i+1]-lst_v[i]:
        len_v = lst_v[i+1]-lst_v[i]
        p3=lst_v[i]
        p4=lst_v[i+1]

print((p2-p1)*(p4-p3))
