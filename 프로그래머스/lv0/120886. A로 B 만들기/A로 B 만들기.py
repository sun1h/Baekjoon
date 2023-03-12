def solution(before, after):
    #before의 "순서"를 바꾸는 것이지 뒤집는 것이 아닙니다.
    return 1 if sorted(before)==sorted(after) else 0