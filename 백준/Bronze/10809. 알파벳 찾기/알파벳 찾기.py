word=input()
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer=[-1 for _ in range(26)]
for i in range(len(word)):
    if word[i] in lst:
        if answer[lst.index(word[i])] == -1:
            answer[lst.index(word[i])] = i
print(*answer)