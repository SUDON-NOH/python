# strings의 요소의 n번째를 기준으로 정렬
# 중복되는 요소는 내림차순으로 정리

def solution(strings, n):

    strings.sort()

    answer = sorted(strings, key=lambda x: x[n])

    return answer