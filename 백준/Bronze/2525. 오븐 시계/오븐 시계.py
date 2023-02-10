hour, minute = map(int, input().split())
cook = int(input())

finish_h = (hour*60 + minute + cook)//60
finish_m = (hour*60 + minute + cook)% 60

finish_h %= 24
# if finish_h >=24 :
#     finish_h = finish_h - 24   

print(finish_h, finish_m)
    