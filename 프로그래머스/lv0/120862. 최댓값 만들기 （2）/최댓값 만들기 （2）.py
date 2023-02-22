def solution(numbers):
    #numbers.sort()
    answer = -10000*10000
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]*numbers[j]  >= answer:
                answer = numbers[i]*numbers[j]
            
    return answer