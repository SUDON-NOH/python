def solution(n):

    x = list(range(1, 1000000))
    a = bin(n).count('1')

    for i in range(len(x)):
        b = bin(x[i])
        b = b.count('1')
        if a == b:
            answer = x[i]

    return answer


print(solution(78))