def solution(phone_number):
    s='*'*(len(phone_number)-4)
    s+=phone_number[len(phone_number)-4:]
    return s