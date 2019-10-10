# 문자열 내림차순으로 배치하기
# 대문자는 소문자보다 작다고 간주

a = 'abDgderhSA'

def solution(s):

    s = ' '.join(s)
    s = s.split()
    s.sort()
    answer = ''

    for i in range(len(s)):

        answer += s[1 * (-i -1)]

    return answer

print(solution(a))

# ===================================================================================

def solution(s):

    return ''.join(sorted(s, reverse=True))

print(sorted(a))
# ['A', 'D', 'S', 'a', 'b', 'd', 'e', 'g', 'h', 'r']

print(sorted(a, reverse = True))
# ['r', 'h', 'g', 'e', 'd', 'b', 'a', 'S', 'D', 'A']

