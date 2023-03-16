def func(arr):
    stack=[]
    for a in arr:
        if a == '(' or a=='[':
            stack.append(a)
        elif stack == [] and (a == ')' or a== ']'):
            return 'no'
        elif stack and a==')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(a)
        elif stack and a==']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(a)
    if len(stack) ==0:
        return 'yes'
    else:
        return 'no'

while True:
    a=input()
    if a == '.':
        break
    print(func(a))