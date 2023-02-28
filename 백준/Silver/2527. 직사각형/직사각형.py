for tc in range(4):
    arr=list(map(int,input().split()))
    if (arr[0]> arr[6] or arr[2]< arr[4]) or (arr[1] > arr[7] or arr[3] < arr[5]):
        print('d')
    elif (arr[2] == arr[4] and arr[3]==arr[5]) or (arr[0] == arr[6] and arr[1]==arr[7]) or (arr[2] == arr[4] and arr[1] == arr[7]) or (arr[6] == arr[0] and arr[3] == arr[5]):
        print('c')
    elif arr[2] == arr[4] or arr[3] == arr[5] or arr[0] == arr[6] or arr[1] == arr[7]:
        print('b')
    else:
        print('a')
