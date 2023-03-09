def solution(polynomial):
    a=0
    b=0
    lst=list(polynomial.split())
    for l in lst:
        if 'x' in l:
            if len(l) == 1:
                a +=1
            else:
                a+=int(l[:-1])
        elif l.isnumeric():
            b += int(l)
    if a !=0 and b!=0:
        if a !=1:
            return f"{a}x + {b}"
        else:
            return f"x + {b}"
    elif a!=0 and b==0:
        if a != 1:
            return f"{a}x"
        else:
            return "x"
    elif a==0 and b!=0:
        return str(b)
    