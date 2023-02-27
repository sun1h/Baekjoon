dic={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
arr=[list(input().split()) for _ in range(20)]
hap=0
gop=0
for i in range(20):
    if arr[i][2] != 'P':
        hap+=float(arr[i][1])
        gop+=(dic.get(arr[i][2])*float(arr[i][1]))
print(gop/hap)