n, m = map(int, input().split())

def f(s):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    f(s + [i])

f([])