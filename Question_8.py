# ======================================================================================================================
# 배열에서 연속되는 값들 중 하나만 남기고 모두 제거

def solution(arr):
    arr.insert(-1, 100)

    for i in range(len(arr)):

        if arr[i + 1] == 100:

            break

        else:
            if arr[i] == arr[i + 1]:

                del arr[i]
                arr.insert(i, 11)

            else:

                pass

    arr.remove(100)

    if arr[-1] == arr[-2]:
        del arr[-1]

    answer = [i for i in arr if i != 11]

    return answer

# ======================================================================================================================

# 효율성 문제
# 간소화

def solution(arr):
    answer = []

    for i in range(len(arr)):

        if i == 0:
            answer.append(arr[i])

        elif arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer