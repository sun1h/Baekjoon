def solution(box, n):
    
    x=box[0]//n
    y=box[1]//n
    z=box[2]//n
    
    answer = x*y*z
    return answer