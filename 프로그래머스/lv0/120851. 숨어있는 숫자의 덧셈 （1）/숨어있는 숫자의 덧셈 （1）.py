def solution(my_string):
    total=0

    for i in range(len(my_string)):
        if my_string[i] in '123456789':
            total+=int(my_string[i])
    return total