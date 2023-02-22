def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+2):
        if n/i==i:
            return 1
            
    return 2