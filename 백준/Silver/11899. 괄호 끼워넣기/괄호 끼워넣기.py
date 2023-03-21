S = input()
stack = []
total = 0
for s in S:
    if s == '(':
        stack.append(s)
    elif s == ')' and stack == []:
        total += 1
    elif s == ')' and stack:
        stack.pop()
if stack != 0:
    total += len(stack)
print(total)
