def solution(hp):
    total=0
    total+=hp//5
    total+=(hp-(hp//5)*5)//3
    total+=((hp-(hp//5)*5)-(hp-(hp//5)*5)//3*3)
    return total