def solution(my_string):
    s=''
    for i in my_string:
        if i.isdigit():
            s+=i
        else:
            s+=' '
    answer=0
    for i in s.split():
        answer+=int(i)

    return answer