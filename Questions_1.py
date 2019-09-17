



def solution(n):
    x = [0, 1]
    if n == 0:
        answer = 0

    elif n == 1:
        answer = 1

    else:
        list_1 = list(range(2, n + 1))
        for i in list_1:
            z = x[i - 1] + x[i - 2]
            x.append(z)

        answer = x[n - 1] + x[n - 2]

    return answer


print(solution(11))

