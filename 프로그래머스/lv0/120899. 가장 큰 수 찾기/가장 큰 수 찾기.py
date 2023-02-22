def solution(array):
    answer = []
    a=sorted(array)
    answer.append(a[-1])
    answer.append(array.index(a[-1]))
    return answer