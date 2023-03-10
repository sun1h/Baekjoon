def solution(spell, dic):
    spell = set(spell) 
    for i in dic:
        if spell.issubset(set(i)): #부분집합
            return 1 
    return 2