def solution(numbers, direction):
    answer = [0]*len(numbers)
    if direction=='right':
        for i in range(len(numbers)):
            answer[i+1-len(numbers)]=numbers[i]
    else:
        for i in range(len(numbers)):
            if i==0:
                answer[-1]=numbers[0]
            else:
                answer[i-1-len(numbers)]=numbers[i]
            
    return answer