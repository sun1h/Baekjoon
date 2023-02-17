def solution(i, j, k):
    answer = 0
    for a in range(i,j+1):
        a=str(a)        
        for j in range(len(a)):
            if a[j]==str(k):
                answer+=1
    return answer