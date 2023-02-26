N=int(input())
num=int(input())
lst=[]
while num >= 1:
    lst.append(num%10)
    num=num//10
print(sum(lst))