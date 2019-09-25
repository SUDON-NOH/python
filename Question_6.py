
def solution(answers):

    count = 0
    point = []
    answer = []

    # (각 사람의 패턴) * (10000개가 되기 위한 배수)
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    # answer의 길이만큼 slicing
    person1 = a[:len(answers)]
    person2 = b[:len(answers)]
    person3 = c[:len(answers)]


    # for문을 돌리기 위해 각 사람을 하나의 리스트로 묶음
    PERSON = [person1, person2, person3]


    # 한 사람의 답안지를 추출
    for person in PERSON:


        # 사람별로 정답을 카운트
        for i in range(len(person)):


            if person[i] == answers[i]:

                count += 1

            else:

                pass

        point.append(count)
        count = 0

    maximum = max(point)

    answer = [(i+1) for i, x in enumerate( point ) if x == maximum]

    return answer


"""
##  좀더 응용한 방법으로 원하는 value가  한리스트 내에 여러개 있을때 이를 모두 구하고 싶다면 다음과 같이 사용하면 된다.

>>> L = [0,1,2,3,1,2,3,1]
>>> target = 1
>>> [ i for i, x in enumerate( L ) if x == target ]
[1, 4, 7]

**  이것은 enumerate()의 멋진 활용이다

L = [0,1,2,3,1,2,3,1] 의 경우나 L = "01231231"의 경우 모두 사용가능하다

즉 list 타입이나 str 타입 모두 응용가능하다
"""






# ======================================================================================================================


def solution(answers):

    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    s = [0] * len(p)
    print(s)

    for q, a in enumerate(answers):
        print('enumerate(answers)', q, a)

        for i, v in enumerate(p):
            print('enumerate(answers)', i, v)
            if a == v[q % len(v)]:
                s[i] += 1
                print(s)

    return [i + 1 for i , v in enumerate(s) if v == max(s)]

answers = [1, 3, 2, 4, 2]

print(solution(answers))
