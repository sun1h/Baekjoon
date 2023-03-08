def solution(common):
    d=0
    r=0
    if common[2] - common[1] == common[1] - common[0]:
        d = common[2] - common[1]
        return common[-1] + d
    elif common[2]//common[1] == common[1]//common[0]:
        r = common[2]//common[1]
        return common[-1]*r