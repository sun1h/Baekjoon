N=int(input())
total=0
while N >=0:
    if N % 5 ==0:
        print(total+N//5)
        break
    else:
        N-=3
        total+=1
else:
    print(-1)