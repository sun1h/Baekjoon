n = int(input())
line = 0
bonso_num = 0
while n > bonso_num:
    line += 1
    bonso_num += line
diff = bonso_num - n
if line%2 == 0: 
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff
print(f'{top}/{bottom}')