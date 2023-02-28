N=input()
n=len(N)
N=int(N)
lst=[]
for i in range(n):
    lst.append(N%10)
    N//=10
lst.sort(reverse=True)
for i in range(n):
    print(lst[i],end='')