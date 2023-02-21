def solution(n):
    lst=[]
    while n > 0:
        lst.append(n%10)
        n=n//10
    answer = 0
    for i in range(len(lst)):
        answer+=lst[i]
    return answer