#1.무한루프안에서 예외처리 해주는법
while True:
    try:
        print(input()) #원하는 처리 해주기
    except EOFError:
    #EOFError: 입력이 끝남(End Of File) 에러
    #데이터가 없어 더 이상 값을 읽을 수 없을 때 발생하는 에러    
        break
'''
while True:
    try:
        print(input())
    except:
        break
똑같다 / 만약 줄이 끝나면 EOFError가 뜰 것이기 때문이다.
'''

#2.sys 모듈을 호출하여 해결 / sys.stdin.readlines()를 사용하면 파일의 끝까지 한번에 가져올 수 있다.
import sys
s = sys.stdin.readlines()
for i in s:
    print(i.rstrip()) #원하는 처리 해주기
