word=input().upper()
w=list(set(word))
lst=[]
for i in range(len(w)):
    lst.append(word.count(w[i]))

l=sorted(lst)
if len(lst) <= 1:
    print(*w)
elif l[-1] == l[-2]:
    print('?')
    exit()
else:
    print(w[lst.index(max(lst))])