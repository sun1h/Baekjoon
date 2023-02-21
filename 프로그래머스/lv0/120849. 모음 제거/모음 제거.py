def solution(my_string):
    my=list(my_string)
    lst=[]
    for i in range(len(my)):
        if my[i] in 'a,e,i,o,u':
            continue
        else:
            lst.append(my[i])
    result= ''.join(lst)
    return result