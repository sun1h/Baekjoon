def solution(lines):
    lst=sum(lines,[])
    mx=max(lst)
    mn=min(lst)
    visit=[0]*(mx-mn+1)
    for i in range(0,len(lst),2):
        for j in range(lst[i+1]-lst[i]):
            visit[lst[i]-mn+j] +=1
    cnt=0
    for i in range(len(visit)):
        if visit[i] > 1:
            cnt+=1

    return cnt