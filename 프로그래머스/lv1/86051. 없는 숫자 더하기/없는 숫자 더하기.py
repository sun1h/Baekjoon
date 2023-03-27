def solution(numbers):
    lst=[i for i in range(10)]
    for n in numbers:
        lst.remove(n)
    return sum(lst)
    
    