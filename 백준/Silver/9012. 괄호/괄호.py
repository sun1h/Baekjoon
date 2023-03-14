def func(lst):
    stack=[]
    for l in lst:
        if l == '(':
            stack.append(l)
        else:
            if len(stack) == 0:
                print('NO')
                return
            else:
                stack.pop()
    if len(stack) !=0:
        print('NO')
    else:
        print('YES')

N=int(input())
for _ in range(N):
    func(input())