def func(idx, turn):
    global lst
    tmp = [0 for _ in range(4)]
    tmp[idx] = turn
    pre_1 = [idx, turn]
    pre_2 = [idx, turn]
    cnt = 0
    while cnt != 4:
        cnt += 1
        if cnt == 4:
            break
        if pre_1[0] - 1 >= 0 and tmp[pre_1[0]] != 0 and lst[pre_1[0]][6] != lst[pre_1[0] - 1][2]:
            if pre_1[1] == 1:
                tmp[pre_1[0] - 1] = -1
                pre_1[1] = -1
            else:
                tmp[pre_1[0] - 1] = 1
                pre_1[1] = 1
        pre_1[0] -= 1

        if pre_2[0] + 1 <= 3 and tmp[pre_2[0]] != 0 and lst[pre_2[0]][2] != lst[pre_2[0] + 1][6]:
            if pre_2[1] == 1:
                tmp[pre_2[0] + 1] = -1
                pre_2[1] = -1
            else:
                tmp[pre_2[0] + 1] = 1
                pre_2[1] = 1
        pre_2[0] += 1

    rotate(tmp)


def rotate(arr):
    global lst
    for i in range(4):
        if arr[i] == 1:
            lst[i].insert(0, lst[i][-1])
            lst[i] = lst[i][:-1]
        elif arr[i] == -1:
            lst[i].append(lst[i][0])
            lst[i] = lst[i][1:]


lst = [[] for _ in range(4)]
for k in range(4):
    for i in input():
        lst[k].append(i)
K = int(input())
move = [list(map(int, input().split())) for _ in range(K)]
for m in move:
    idx, turn = m
    func(idx - 1, turn)

total = 0
score = [1, 2, 4, 8]
for i in range(4):
    if lst[i][0] == '1':
        total += score[i]

print(total)
