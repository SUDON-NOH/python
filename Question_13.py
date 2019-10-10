# s 의 길이가 4 or 6
# 숫자만으로 되었으면 True
# 아니면 False

def solution(s):

    if len(s) == 4 or len(s) == 6:
        try:
            a = int(s)
            answer = True

        except ValueError:
            answer = False

    else:
        answer = False

    return answer

# ===============================================================

def solution(s):
    return s.isdigit() and len(s) in (4, 6)

a = 'a123'
b = '1234'

print(b.isdigit())      # 숫자만 존재하면 True, # 문자가 포함되어 있으면 False
print(len(a) in (4, 6)) # 길이가 4 or 6 이면 True, 아니면 False