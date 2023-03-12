def solution(emergency):
    answer = [1]*len(emergency)
    for i in range(len(emergency)-1):
        for j in range(i,len(emergency)):
            if emergency[i] > emergency[j]:
                answer[j] +=1
            elif emergency[i] < emergency[j]:
                answer[i]+=1
    return answer