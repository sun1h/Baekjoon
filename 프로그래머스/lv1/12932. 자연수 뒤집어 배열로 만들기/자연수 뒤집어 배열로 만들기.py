def solution(n):
    n=str(n)
    answer = []
    for i in range(len(n))[::-1]:
        answer.append(int(n[i]))
    return answer