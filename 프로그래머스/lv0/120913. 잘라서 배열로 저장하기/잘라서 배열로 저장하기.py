def solution(my_str, n):
    answer = []
    tmp=''
    N=len(my_str)
    while N > n:
        if len(tmp) == n:
            answer.append(tmp)
            tmp=''
            N=N-n      
        else:    
            tmp+=my_str[0]
            my_str=my_str.replace(my_str[0],'',1)   
    if N !=0:
        for i in range(N):
            tmp+=my_str[i]
        answer.append(tmp)
    return answer