def solution(s):
    n=len(s)//2
    if len(s)%2:
        return s[n]
    else:
        lst=s[n-1],s[n]
        return ''.join(lst)