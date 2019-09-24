a = [1, 5, 2, 6, 3, 7, 4]
b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    y = []

    for x in range(len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        print('i', i)
        print('j', j)
        print('k', k)
        a = array[i - 1:j]
        a.sort()
        print('a', a)

        y.append(a[k-1])

    answer = y

    return answer

print(solution(a, b))