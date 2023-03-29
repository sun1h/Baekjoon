def solution(sizes):
    x=0
    y=0
    for s in sizes:
        if x < max(s):
            x=max(s)
        if y < min(s):
            y=min(s)
    return x*y
                