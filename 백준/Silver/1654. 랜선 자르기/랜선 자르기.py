K,N=map(int,input().split())
lst=[int(input()) for _ in range(K)]
start,end=1,max(lst) # 1을 시작, 최댓값을 끝
while start <= end:  # 반복문 종료 조건
    mid=(start+end)//2 # 중앙 원소 고르기
    total=0 # 랜선 갯수
    for l in lst:
        total += l // mid # 중앙값 만큼 랜선을 자르면 얻을 수 있는 최대 갯수 = 랜선길이 // 중앙값
    if total >= N:
        start=mid+1
    else:
        end= mid-1
print(end)

