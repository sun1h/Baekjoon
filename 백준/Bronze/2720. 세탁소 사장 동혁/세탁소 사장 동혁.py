for tc in range(int(input())):
    t=int(input())
    price=[25,10,5,1]
    cnt=[0 for _ in range(4)]
    i=0
    while 4>i >=0:
        if t >= price[i]:
            t-=price[i]
            cnt[i]+=1
        else:
            i+=1
    print(*cnt)