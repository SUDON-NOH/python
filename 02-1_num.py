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
\n                 : 줄바꾸기
\t                 : Tab 키 같은 기능
CTRL + D           : 라인 복사
CTRL + W           : 라인 전체 선택
CTRL + F2          : Stop
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
time = int(dist) / int(vel)
print(time)

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
SC = (int(HWC) - 32) / 1.8
print(format(int(SC), '4.2f'))

# Q4
a = input('a = ')
b = input('b = ')
sum_1 = int(a) + int(b)
sub_1 = int(a) - int(b)
mul_1 = int(a) * int(b)
dvi_1 = int(a) / int(b)
mok_1 = int(a) // int(b)
nah_1 = int(a) % int(b)

print('{0} = {1}'.format('합', sum_1))
print('{0} = {1}'.format('차', sub_1))
print('{0} = {1}'.format('곱', mul_1))
print('{0} = {1}'.format('나누기', dvi_1))
print('{0} = {1}'.format('몫', mok_1))
print('{0} = {1}'.format('나머지', nah_1))


#numeric_ex.py

#1번
print( '{0:=^50}'.format( '1번' ) )
velocity = input( 'Input velocity : ' )
distance = input( 'Input distance : ' )

#time = eval( distance + '/' + velocity )
time = int(distance) / int(velocity)

print()
print( 'velocity : {0:<6.2f}'.format( float( velocity ) ) )
print( 'distance : {0:<6.2f}'.format( float( distance ) ) )
print( 'time     : {0:<6.2f}'.format( time ) )

#2번
print( '{0:=^50}'.format( '2번' ) )
length = input( 'Input length : ' )
width = input( 'Input width : ' )

#area = eval( length + '*' + width )
area =  int(length) * int(width)
#circumference = eval( length + '*' + '2' + '+' + width + '*' + '2' )
circumference =  int(length) * 2 + int(width) *2

print()
print( 'length : {0:<6.2f}\twidth : {1:<6.2f}'.format( float( length ), float( width ) ) )
print( 'area : {0:<6.2f}'.format( area ) )
print( 'circumference : {0:<6.2f}'.format( circumference ) )

#3번
print( '{0:=^50}'.format( '3번' ) )
fahrenheit = float( input( 'Input fahrenheit : ' ) )

celsius = ( fahrenheit - 32 ) / 1.8

print()
print( 'fahrenheit : {0:<6.2f} -> celsius : {1:<6.2f}'.format( fahrenheit, celsius ) )

#4번
print( '{0:=^50}'.format( '4번' ) )
number1 = int( input( 'Input number1 : ' ) )
number2 = int( input( 'Input number2 : ' ) )

add = number1 + number2
subtract = number1 - number2
multiple = number1 * number2
divide = number1 / number2
mod = number1 % number2

print()
print( '{0:^6} + {1:^6} = {2:<6}'.format( number1, number2, add ) )
print( '{0:^6} - {1:^6} = {2:<6}'.format( number1, number2, subtract ) )
print( '{0:^6} * {1:^6} = {2:<6}'.format( number1, number2, multiple ) )
print( '{0:^6} / {1:^6} = {2:<6.2f}'.format( number1, number2, divide ) )
print( '{0:^6} % {1:^6} = {2:<6.2f}'.format( number1, number2, mod ) )

print("-"*70)

# bool : True는 1 False는 0 정수 값으로 간주된다.

a = 1
print(a > 0) # True
print(a < 0) # False

b = a > 0
print(b)
print(type(b))
print(type(a))

c = True
print(type(c))

C = True + True
print(c, type(c))

C = True + b            # True
print(b, type(c))

d = bool(3)             # True
print(d, type(d))

e = bool(0)             # False
print(e, type(e))

f = bool([])            # False
print(f, type(f))

g = bool([0])           # True
print(g, type(g))
