arr=list(map(int,input().split()))
if arr == [i for i in range(1,9)]:
    print('ascending')
elif arr == [i for i in range(1,9)[::-1]]:
    print('descending')
else:
    print('mixed')