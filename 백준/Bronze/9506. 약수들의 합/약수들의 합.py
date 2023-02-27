while True:
    n=int(input())
    if n == -1:
        break
    lst=[]
    for i in range(1,n):
        if n % i ==0:
            lst.append(i)
    if sum(lst) == n:
        print(n,'=',end=' ')
        for i in range(len(lst)-1):
            print(lst[i],'+',end=' ')
        print(lst[-1])

    else:
        print(f'{n} is NOT perfect.')