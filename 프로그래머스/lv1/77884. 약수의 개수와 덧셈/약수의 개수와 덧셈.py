def solution(left, right):
    tmp=0
    for i in range(left,right+1):
        lst=[]
        for j in range(1,i+1):
            if i % j == 0:
                lst.append(j)
        if len(lst)%2==0:
            tmp += i
        else:
            tmp-= i
    return tmp