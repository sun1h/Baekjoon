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
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True