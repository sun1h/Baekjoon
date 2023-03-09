def solution(board):
    n=len(board)
    dx=[0,0,1,-1,1,-1,1,-1]
    dy=[1,-1,0,0,1,-1,-1,1]
    
    lst=[]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                lst.append((i,j))
    
    for i,j in lst:
        for k in range(8):
            if 0<=(i+dx[k])<n and 0<=(j+dy[k]) <n:
                board[i+dx[k]][j+dy[k]] = 1
            
    cnt=0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt+=1
    
    return cnt
                
    
    
        
    
    