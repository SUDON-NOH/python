
def solution(s):

    if len(s)%2==1:
        answer=s[len(s)//2]

    else :
        answer= s[len(s)//2-1]+s[len(s)//2]

    return answer

# =====================================================================================================================


def solution(str):

    return str[(len(str)-1)//2 : len(str)//2+1]

print(solution('power'))


x = 'powers'

print((len(x)-1)//2)
print((len(x)//2+1))
print(x[2:4])