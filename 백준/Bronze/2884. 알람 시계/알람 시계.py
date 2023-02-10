H,M=map(int, input().split())
if H != 0:

    if 60> M>=45:
        M = M -45
        print(H,M)
    else:
        H = H-1
        M = M + 15   
        print(H,M)
else:
    if 60> M>=45:       
        M = M -45
        print(H,M)
    else:
        H = 23
        M = M + 15
        print(H,M)
