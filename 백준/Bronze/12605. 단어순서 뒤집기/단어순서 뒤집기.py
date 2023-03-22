N=int(input())
for x in range(1,N+1):
    lst=input().split()
    print(f'Case #{x}:', *lst[::-1])