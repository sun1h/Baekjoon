def solution(s):
    s=list(s.split())
    print(s)
    answer = 0
    tmp=''
    for i in range(len(s)):
        if s[i] == 'Z':
            answer -= int(s[i-1])
        else:
            answer+= int(s[i])
    return answer