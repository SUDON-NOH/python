def solution(n, lost, reserve):
    for i in lost:

        if i in reserve:

            reserve.remove(i)
            lost.remove(i)

        else:

            pass

    for i in lost:

        if i in reserve:

            reserve.remove(i)

        elif i - 1 in reserve:

            reserve.remove(i - 1)

        elif i + 1 in reserve:

            reserve.remove(i + 1)

        else:

            n -= 1

    return n