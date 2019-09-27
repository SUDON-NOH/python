# s 라는 문자열을 받고 p의 수와 y의 수가 같으면 True를 반환
# 대문자 소문자 섞여있으나 구분없이 개수를 센다

def solution(s):
    s=s.lower()
    if s.count('p') == s.count('y'):
        answer=True
    else:
        answer=False
    return answer