def solution(x, n):
    answer = []
    if x != 0:
        for i in range(x,x*(n+1),x):
            answer.append(i)
        return answer
    else:
        return [0 for _ in range(n)]