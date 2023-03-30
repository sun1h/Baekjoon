tmp="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n,b=map(int,input().split())
answer=''
while n!=0:
    i=n%b
    answer+=str(tmp[i])
    n//=b
print(answer[::-1])