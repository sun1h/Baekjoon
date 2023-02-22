def solution(numbers):
    numbers.sort()
    #[-5, -3, 1, 2, 4]
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
