N,L=map(int,input().split())
total=0
pre=0
for _ in range(N):
    D,R,G=map(int,input().split())
    if pre == 0:
        total += D
        pre = D
    else:
        total += D - pre
        pre=D
    #현재 신호등 불 판별
    remainder = total % (R+G)
    if remainder - R <= 0: #빨간불 켜짐
        total += R - remainder
total += L - pre
print(total)
