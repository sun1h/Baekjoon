N=int(input())
for n in range(N):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    alst=[0,0,0,0]
    blst=[0,0,0,0]
    for i in range(1,len(a)):
        alst[a[i]-1] +=1
    for i in range(1,len(b)):
        blst[b[i]-1] +=1
    
    tmp=0
    for i in range(4)[::-1]:
        if alst[i] > blst[i]:
            print('A')
            break
        elif alst[i] < blst[i]:
            print('B')
            break
        else:
            tmp+=1

    if tmp ==4:
        print('D')