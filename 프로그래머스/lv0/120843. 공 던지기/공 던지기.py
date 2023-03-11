
def solution(numbers, k):
    idx = 0
    for i in range(k-1):
        idx += 2
        idx %= len(numbers)

    return idx + 1
