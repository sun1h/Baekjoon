A = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
total = 0
for i in range(len(word)):
    for j in range(len(A)):
        if word[i] in A[j]:
            total += j+3
print(total)