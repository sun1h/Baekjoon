lst = input()
total = 0  # 잘려진 조각의 갯수
pre = 0  # 레이저인지 아닌지 판별하기 위해 그 전값과 현재값이 ( ) 인지 확인하기 위해 그 전 값 저장
stack = []
for l in lst:
    if l == '(':
        stack.append(l)
    elif l == ')' and pre == '(':  # 레이저 () 를 만난다면
        stack.pop()  # 레이저 쌍 중 stack에 저장되어 있는 ( 제거
        total += len(stack)  # 겹쳐져 잘려진 쇠막대기 갯수 (stack에 쌓여있는 만큼 추가)
    else:  # 레이저의 끝단과 쇠막대기 오른쪽 끝을 의미하므로 나올때 마다 +1
        stack.pop()  # 해당 쇠막대기는 왼쪽 끝에서 오른쪽 끝까지 다 살폈으므로 제거
        total += 1
    pre = l  # 그 전 값 비교
print(total)