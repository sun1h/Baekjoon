def check(y,x): # 이동할 수 있는지 확인하고 이동할 수 있다면 이동하는 함수
    global kx,ky,sx,sy
    nx_k=kx+x
    ny_k=ky+y
    if nx_k<0 or ny_k<0 or nx_k>=8 or ny_k>=8:
        return
    else:
        if nx_k == sx and ny_k==sy:
            nx_s=sx+x
            ny_s=sy+y
            if nx_s<0 or ny_s<0 or nx_s>=8 or ny_s>=8:
                return
            else:
                kx = nx_k
                ky = ny_k
                sx = nx_s
                sy = ny_s
        else:
            kx=nx_k
            ky=ny_k

lst_x=['A','B','C','D','E','F','G','H']  # x좌표의 문자를 인덱스 숫자로 바꾸기 위해 리스트 생성
dic={'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0],'RT':[1,1],'LT':[1,-1],'RB':[-1,1],'LB':[-1,-1]} #이동방향 설정
k,s,N=input().split()
kx=lst_x.index(k[0]) #문자 x좌표를 숫자 인덱스로 전환
ky=int(k[1])-1 # y좌표: 1부터 시작하나 x좌표 인덱스가 0부터 시작하므로 같이 맞춰주기 위해 -1
sx=lst_x.index(s[0])
sy=int(s[1])-1
for i in range(int(N)):
    n=input()
    [y,x]=dic[n]  # 입력값이 의미하는 이동경로를 숫자로 전환
    check(y,x)  
K=[lst_x[kx],str(ky+1)] 
S=[lst_x[sx],str(sy+1)]
print(''.join(K))
print(''.join(S))
