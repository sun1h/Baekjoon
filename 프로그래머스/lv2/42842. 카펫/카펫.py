def solution(brown, yellow):
    tmp=brown+yellow
    answer = 0
    for i in range(1,max(brown,yellow))[::-1]:
        if yellow/i+i==brown/2-2:   
            answer=[i+2,tmp/(i+2)]
            break
    return answer