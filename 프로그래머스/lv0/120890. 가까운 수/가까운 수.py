def solution(array, n):
    answer = 0
    
    array.sort()
    
    record = 987654321
    for i in array:
        diff = abs(n - i)
        if diff < record:
            record = diff
            answer = i
        
    return answer