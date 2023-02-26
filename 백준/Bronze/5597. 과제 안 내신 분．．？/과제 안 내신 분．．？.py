lst=[i+1 for i in range(30)]
for _ in range(28):
    n=int(input())
    if n in lst:
        lst.remove(n)
print(lst[0])
print(lst[-1])