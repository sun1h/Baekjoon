N=int(input())
total=0  # 직사각형 갯수
for i in range(1,N+1): #가로 영역 1~N
    for j in range(i, N//i+1): # 세로 영역 1~N//i인데 겹치는 경우 제외를 위해 i~N//i 까지 지정
        total+=1

print(total)
