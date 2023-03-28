def solution(arr):
    answer = []
    for a in arr:
        if not answer or answer[-1] != a:
            answer.append(a)            
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer