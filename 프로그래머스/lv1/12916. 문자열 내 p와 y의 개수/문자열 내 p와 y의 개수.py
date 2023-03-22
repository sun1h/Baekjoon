def solution(s):
    answer = True
    s = s.lower()
    a,b=0,0
    for i in s:
        if i == 'p':
            a+=1
        elif i=='y':
            b+=1
    if a == b:
        return True
    else:
        return False
    