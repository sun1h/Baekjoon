result="wrong"
while True:
    arr=list(map(int,input().split()))
    if arr==[0,0,0]:
        break
    arr.sort()
    if arr[-1]**2==arr[0]**2+arr[1]**2:
        result="right"
    print(result)
    result = "wrong"