def solution(answers):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    total = 0
    tmp = [0, 0, 0]
    cnt = [0, 0, 0]
    while total <= len(answers) - 1:
        tmp[0] %= len(n1)
        tmp[1] %= len(n2)
        tmp[2] %= len(n3)

        if answers[total] == n1[tmp[0]]:
            cnt[0] += 1
        if answers[total] == n2[tmp[1]]:
            cnt[1] += 1
        if answers[total] == n3[tmp[2]]:
            cnt[2] += 1

        total += 1
        tmp[0] += 1
        tmp[1] += 1
        tmp[2] += 1

    result = []
    mx = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == mx:
            result.append(i + 1)
            
    return result
