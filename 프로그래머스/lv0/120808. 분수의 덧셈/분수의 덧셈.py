def solution(numer1, denom1, numer2, denom2):
    numer=numer1*denom2+numer2*denom1
    denom=denom1*denom2
    
    gcd=0 #greatest common divisor
    for i in range(min(numer,denom),0,-1):
        if numer%i==0 and denom%i==0:
            gcd=i
            break
            
    answer = [numer//gcd, denom//gcd]
    return answer


'''
a=6
b=8

for i in range(min(a,b),a*b):
    if i%a==0 and i%b==0:
        lcm=i
        break

print(lcm)
'''