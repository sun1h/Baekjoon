def solution(id_pw, db):
    tmp=0
    for i in range(len(db)):
        if id_pw == db[i]:
            return "login"   
        elif id_pw[0] != db[i][0]:
            tmp+=1
    if tmp == len(db):
        return "fail"
    elif tmp < len(db):
        return "wrong pw"