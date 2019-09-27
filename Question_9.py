# a, b 사이의 정수들의 합
# a, b의 크기는 정해지지 않음


def solution(a, b):
    if a <= b:

        answer = sum(range(a,b+1))

    else:

        answer = sum(range(b, a+1))

    return answer