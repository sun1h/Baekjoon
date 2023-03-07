def solution(babbling):
    answer = 0
    for b in babbling:
        temp = ''
        while len(b) > 0:
            if b[:3] == 'aya' and temp != 'aya':
                b = b[3:]
                temp = 'aya'
            elif b[:3] == 'woo' and temp != 'woo':
                b = b[3:]
                temp = 'woo'
            elif b[:2] == 'ye' and temp != 'ye':
                b = b[2:]
                temp = 'ye'
            elif b[:2] == 'ma' and temp != 'ma':
                b = b[2:]
                temp = 'ma'
            else:
                break
        if len(b) == 0:
            answer += 1
    return answer
