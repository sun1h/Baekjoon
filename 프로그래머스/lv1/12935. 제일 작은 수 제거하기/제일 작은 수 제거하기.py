def solution(arr):
    answer = []
    m=arr[0]
    for i in range(1,len(arr)):
        if arr[i] < m:
            m=arr[i]
    for a in arr:
        if a != m:
            answer.append(a)
    if not answer:
        answer.append(-1)
    return answer