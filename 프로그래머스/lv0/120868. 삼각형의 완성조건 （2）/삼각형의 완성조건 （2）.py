def solution(sides):
    sides.sort()
    total=0
    for i in range(sides[1]-sides[0],sides[0]+sides[1]):
        if i+sides[0] >sides[1] and i <= sides[1]:
            total+=1
        elif sides[0]+sides[1]>i and i >=sides[1]:
            total+=1
    return total