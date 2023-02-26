T=int(input())
for tc in range(T):
    R,word=input().split()
    lst=[]
    for i in range(len(word)):
        lst.append(word[i]*int(R))
    print(''.join(lst))