def solution(n):
    for i in range(1,n+1):
        if int((6*i)/n)==(6*i)/n and (6*i)/n >=1:
            return i
        