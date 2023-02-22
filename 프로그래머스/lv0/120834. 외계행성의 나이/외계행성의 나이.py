def solution(age):
    age=list(str(age))
    answer = []
    dic=dict(zip(['0','1','2','3','4','5','6','7','8','9'],['a','b','c','d','e','f','g','h','i','j']))
    for i in range(len(age)):
        val=dic.get(age[i])
        answer.append(val)
    answer=''.join(answer)
    return answer