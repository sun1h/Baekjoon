n=int(input())
lst=[]
for _ in range(n):
    x,situ = input().split()
    if situ == 'enter':
        lst.append(x)
    elif situ == 'leave':
        lst.remove(x)
lst.sort(reverse=True)
for i in range(len(lst)):
    print(lst[i])