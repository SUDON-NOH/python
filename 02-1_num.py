# 단축키
"""
CTRL + /           : 주석문 설정 / 해제
Tab                : 들여쓰기(Indent)
Shift + Tab        : 들여쓰기 해제(Unindent)
Shift + F10        : 기존 수행했던 소스코드를 Run
CTRL + Shift + F10 : 현재 수행 중인 소스코드를 Run
Shift + F9         : Debug
F8                 : Debug Step Over
Alt + Shift + E    : 한 줄씩 또는 블럭한 것들만 출력
"""

# 02-1_숫자형

# 표준 입출력
# 표준 입력 : 변수 = input("문자열")

a = input()
print(a)

# Pycharm 에서는 코드를 중간부터 시작하는 기능은 없다. 중간부터 실행하려면 위의 코드들을 주석처리 혹은 Jupyter Notebook 사용

math = input("수학점수:")                     # 문자열(str) 타입을 반환
english = input("영어점수:")                  # 문자열(str) 타입을 반환
total = int(math) + int(english)            # 문자열을 숫자로 형변환
print('총점:', total)

# 표준 출력 : print()
print('add : ', 4 + 5, 'sub = ', 4 - 2)      # \n : 마지막에 다음 줄로 이동해라 / 코드의 끝에는 항상 \n 으로 줄 바꿈
print(1, 2) ; print(3,4)                     # ; : 한 문장에 여러 코드를 출력할 때 사용 / 출력시 줄 바꿈
print(1, 2, end = ' ')                       # \n 대신에 end에 공백을 넣어 줄을 바꾸지 않고 1 2 5 6 7 을 한 줄에 표현
print(5, 6, 7)
print(1, 2, end = " 또 ")
print(5, 6, 7)
print(5, 6, 7, sep = ',')                    # sep = 개체 사이사이에 들어갈 값을 입력 / 원래는 공백으로 지정되어 있음

# print() formatting
num_1 = 10
num_2 = 1.234
str_1 = "Hello python"
print("%d" % num_1)        # %d int 형
print("%f" % num_2)        # %f float 형
print("%x" % num_1)        # %x 16진수  /  0x%x 의 형태로 많이 표현
print("%o" % num_1)        # %o 8진수
print("문자열 : %s"%str_1)

print("int 형: %d" % num_1)
print("float 형 : %f" % num_2)
print("16진수 : %x" % num_1)
print("8진수: %o" % num_1)

print("문자열: %s int형: %d"%(str_1,num_1)) # 2가지 이상 출력

# format() 함수 사용
print(format(1.234567, "10.3f"))          # "10.3f" 에서 10은 소수점 포함 전체 자릿수, 3f는 소수점 자릿수
print(format(1.2345678, "7.4f"))

print('{0} {1}'.format('apple', 7.77))    # index 0번과 1번을 출력
print('{0}/{1}'.format('apple', 7.77))

print('{0:<10}{1:5.2f}'.format('apple', 7.77))   # 0번 index 10자리 왼쪽부터 정렬, 1번 index 소수점 포함 5자리 소수점 아래 2자리 표현
print('{0:>10}{1:5.2f}'.format('apple', 7.77))   # 오른쪽 정렬
print('{0:^10}{1:5.2f}'.format('apple', 7.77))   # 가운데 정렬
print('{0:=<10}{1:5.2f}'.format('apple', 7.77))  # 공백에 =을 입력
print('{0:=>10}{1:5.2f}'.format('apple', 7.77))
print('{0:=^10}{1:5.2f}'.format('apple', 7.77))


# 숫자형 변수
a = 12345

# int형 : 정수형
print(int(a))
print(bin(15))      # 2진수
print(hex(15))      # 16진수
print(oct(15))      # 8진수

# 1111[2진수] 계산
# 8421      2의 3승, 2의 2승, 2의 1승, 2의 0승 을 전부 더해서 15
# 15[10진수]
# F[16진수]
# 0~9 A B C D E F : 16진수로 표현했을 때 0부터 15까지의 수 표현

# 1010
# 8421
# 10[10진수]
# A[16진수]

# float형 : 실수형
print(float(a))

# complex형 : 복소수형
print(complex(a))    # (12345+0j)

print(float('inf'))  # 무한대
num = float('inf')
print(num/1000)      # inf / 수 => inf
print(1000/num)      # 수 / inf => 0   :   0으로 수렴
print(num/num)       # inf / inf => nan, Not a Number 결측치와 같은 개념이 된다
print(float('nan'))  # 'nan'


# 사칙연산 : + , - , * , / , % , //
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b           # 나머지
h = a // b          # 몫
i = a ** b          # a의 b제곱 ex)10의 3승

print("Hello" * 3)  # 문자에 곱셈을 하면 반복이 된다
print("-" * 50)


# 숫자형 실습문제
# Q1
print('{0:=^60}'.format('Q.1'))

dist = input("거리 : ")
vel = input("속도 : ")
dist_vel = int(dist) / int(vel)
print(dist_vel)

# Q2
print('{0:=^60}'.format('Q.2'))
LGT = input("길이 : ")
ABC = input("너비 : ")
M = int(LGT) * int(ABC)
print('{0}={1}'.format('면적', M))

ROD = int(LGT) * 2 + int(ABC) * 2
print('{0}={1}'.format('둘레', ROD))

# Q3
print('{0:=^60}'.format('Q.3'))
HWC = input("화씨 : ")
SC = input("섭씨")

