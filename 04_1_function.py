# 04-1_함수
"""
함수
2019-07-08
"""
# 정의 : 입력값을 가지고 어던 일을 수행한 다음, 그 결과물을 내어놓는 것
# 얘: 과일 - 입력, 믹서 - 함수, 주스 - 출력
# 장점 : 재사용
# 유래 : 퍼셉트론 - 뉴런
# 모듈과 함수
    # 함수자체가 모듈(library)
    # class 안 함수 = method
# 함수 구조
    # def 함수명(인자):
        # 1. <수행 문장 1>
        # 2. <수행 문장 2>

a = 10
b = 20
c = a + b
print('a + b = %d' % c)

# 10회 덧셈 반복
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for k in range(len(a)):
    print(k,':', a[k] + b[k])


# 함수 구현
# add() 함수 정의
def add(a, b):
    c = a + b
    print('add called!!')
    return c

result = add(10, 20) # 함수호출
print(result)
print('Exit')


# substract() 함수 정의
def sub(a, b):
    sub_result = a - b
    return sub_result

# multiply() 함수 정의
def mul(a , b):
    mul_result = a * b
    return mul_result

# divide() 함수 정의
def div(a , b):
    div_result = a/b
    return div_result

sub_result = sub(10 , 20)
mul_result = mul(10 , 20)
div_result = div(10 , 20)

print( "sub_result: {0}, mul_result : {1}, div_result : {2}"
       .format(sub_result,mul_result,div_result))

# 응용
# 함수내에서 함수 호출하는 함수 구현

# "연산자 사용 함수"
#myfunc(a,b,c,d,e) = ((a+b)*(c-d))/e

# 1. 함수내에서 직접 연산
def myfunc1(a,b,c,d,e):
    if e==0 : return "e is 0. Div error"
    f =  ((a+b)*(c-d))/e
    return f
result = myfunc1(1,2,6,4,2)
print(result)

#2. add/ subtract/ multiply / divide 함수 사용
# "정의한 함수 사용 "

def myfunc2(a,b,c,d,e):
    if e==0 : return "e is 0. Div error"
    f =  div(mul(add(a,b),sub(c,d)),e)
    return f
result_2 = myfunc2(1,2,6,4,2)
print(result_2)

# 함수 구현 순서
# (1) def 를 사용하고 함수이름을 결정
# (2) 매개변수(parameter)와 인수(argumens)
"""        ex) def add(a, b):    <- a, b는 매개변수
             return a + b
           print(add(3,4)    <- 3, 4는 인수        """
# (3) 인자를 사용하여 처리하는 코드를 구현
# (4) return을 사용하여 결과값을 반환
# ----------------함수 구현--------------------
# (5) 인수를 설정하여 함수를 호출하여 결과를 확인

# 함수 유형 4가지
# [1] 반환값이 없고, 매개 변수 없고
"""     내가 정의한 함수에 print()가 입력되어 있으면
        따로 print를 할 필요가 없지만
        return 값만 주어진 경우는 따로 print를 입력해야 한다     """

def f_1():
    print('f_1 is called!!')

print(f_1())

# [2] 반환값이 없고, 매개 변수 있고

def f_2_1(a , b):
    print('f_2:', a, b, a + b, a - b, a * b, a/b)
f_2_1(12 , 34)

def f_2_2(a1, a2, a3 = 'None'):          # 변수가 3개   # a3 = 'None', 기본 인자
    print('f_2_2:', a1, a2, a3)          # 변경가능     # '=': 값이 없으면 = 다음의 값을 입력
f_2_2(10, 20, 30)
f_2_2(10, 20)


# [3] 반환값이 있고, 매개 변수 없고

def f_3():
    print('f_3 is called!')
    return 'bread','Butter'     # <- 값을 입력 하면 튜플이든 리스트이든 만들 수 있다
print(f_3())

# [4] 반환값이 있고, 매개 변수 있고

def f_4(a, b):
    return a + b, a * b
print(f_4(1, 2))

# 문제 : 2개의 정수에 대해 큰 수, 작은 수의 순서로 반환
#       하는 함수를 만드세요. 함수이름은 order()

def order(a, b):
    if a < b:
        a, b = b, a
    return a, b
order(19, 1)
order(2, 94)

def order_2(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    return a, b
order_2(66, 52)
order_2(22, 106)

# 문제 : max() 함수, min() 함수, sum() 함수를 만드세요.

# max(a, b) 함수

def max_2(a, b):
    if a > b:
        return a
    return b

# min(a, b) 함수

def min_2(a, b):
    if a > b:
        return b
    return a

# sum(list) 함수

def sum(l):
    total = 0
    for k in l:
        total = total + k
    return total

print(sum([1, 2, 3, 4, 5]))

# mean(list) 함수

def mean(l):
    total = 0
    for k in l:
        total = total + k
    return total/len(l)

def mean_2(l):
    return sum(l)/len(l)

print(mean([10, 20, 30, 40, 50]))
print(mean_2([10, 20, 30, 40, 50]))

# 인수의 개수와 고정되지 않은 인수 처리 방법

def add_many(*args):                        # *args <- 리스트 객체의 개수가
    total = 0                               #          정해지지 않은 경우 사용
    for k in args:
        total = total + k
    return total
print(add_many(10, 20, 30, 40, 50, 60))

# 키워드 인수(사전 사용)
# (2) **변수 : dict 형식
def func(width, height, **kw):
    print(width, height)
    print(kw)
func(10,20,depth = 5, dimension = 7)

# 함수 사용시 변수의 유효범위 규칙(Scope Rule)
# LEGB 규칙: Local > EnclosingFuncion Local
#           > Global > Buillt-in
x = 10  # 전역변수(Global Variable)
y = 11  # 전역변수(Global Variable)
def foo():
    x = 20  # L : 지역변수(Local variable)
    foo_list = [1, 2]   # L : 지역변수(Local variable)
    def bar():
        a = 30  # L : 지역변수(Local variable)
        print('bar:', a, x, y) # a:L, x:E(함수 바깥에, 그러나 foo 라는 함수 안에) , y:G
        # bar : 30 20 11
    bar()

foo()

# 주의해야 할 변수 사용
# 함수안에서 다른 함수에서 사용하는 지역변수를 사용하는 것
# def foo2():
#     foo_list[0]= 10



# 일급 함수(First Class function)
# (1) 함수 객체를 다른 함수의 인수로 전달할 수 있다.


def add_two(a, b):
    print('add_two is called')
    return a + b

def func_two(func, a, b):
    print('func_two is called')
    result = func(a, b)
    return result

result = func_two(add_two, 10, 20)
print(result)

# (2) 함수 객체를 반환 값으로 전달할 수 있다.

def foo2():
    print('foot2 is called!!')
    def bar2():
        print('bar2 is called!!')
    return bar2         # 함수 객체를 반환
result = foo2()
print(type(result))     # <class 'function'>
result()                # bar2 is called!! bar2()함수 호출

# (3) 함수 객체를 다른 자료구조에 저장해서 사용 가능하다.

func_list = [add, sub, mul, div]
result = func_list[0](10, 20)   # add(10, 50)
print(result)                   # 함수를 리스트 안에 넣을 수 있다

result = func_list[1](10, 50)   # sub(10, 50)
print(result)

c = add
c(1, 2)
d = c
d(3, 4)
print(c)
print(d)



# 람다(Lambda) 함수 : 한줄짜리 함수
# 식을 정의하는 순간 바로 함수 객체로 사용
# 바로 인수로 전달한다.
# 함수명 = lambda 인수1, 인수2, ... : < 반환할 식 >
# def add_new(a, b):
#     return a + b
                        # 위와 아래는 같은 함수이다.
add_new = lambda a, b: a + b
result = add_new(7, 10)
print(result)


def f1(x):
    return x*x+1
def g(func):
    return [func(x) for x in range(1, 5)]
print(g(f1))

print([f1(x) for x in range(1, 5)])
print([f1(1), f1(2), f1(3), f1(4)])

# 람다식 함수 선언
print(g(lambda x : x * x + 1)) # 람다 함수 사용



# 파이썬 내장 함수(Built-in : 이미 저장되어 있는 함수)
# (1) map 함수
def multi_two(x):
    return x * 2

result = map(multi_two, [1, 2, 3, 4, 5])
print(list(result))         # [2, 4, 6, 8, 10]

# (2) abs() : 절대값을 구해주는 함수
print(abs(-1234))       # |-1234| -> 1234
print(abs(1234))        # |-1234| -> 1234
print(abs(0))           # |0| -> 0

# (3) chr(숫자) : 아스키 코드 문자  <- 인터넷에서 아스키 코드 리스트를 볼 수 있음
print(chr(97))  # --> 'a'
print(chr(48))  # --> '0'
    # 아스키 코드 1 ~ 255 까지 코드값과 해당 문자가 나오게 출력
for k in range(1, 255):
    print(chr(k),':', k, end = ' , ')
    if k % 10 == 0:
        print()
    else:
        pass

# globals()/locals() : 전역/지역 심볼테이블을 얻는다.
print(globals())
print(locals())

# ard() : 문자의 아스키 값을 반환
print(ord('a'))      # 97
# max()/min()/sum()/round()/pow()
# id() : 개체의 참조 주소 값을 반환
print(list(zip([1,2,3],[5,6,7])))
print(list(zip([1,2,3],['a','b','c'],[5,6,7])))
# [(1, 'a', 5), (2, 'b', 6), (3, 'c', 7)]

# 외장함수 -> 파이썬 데이터 분석 강의중에 다룬다


print("{0:=^70}".format('함수 문제'))

# title = '성적테이블'
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# count = 0
# number = 4
# print(title)
# for k in l:
#     count = count + 1
#     print(k, end = ' ')
#     if count % number == 0:
#         print()

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def printList(title, numberPerLine, prnList):
    count = 0
    print('{0:=>20}:{1:=<20}'.format('성적', title))
    for k in prnList:
        count = count + 1
        print('{0:^10}'.format(k), end = ' ')
        if count % numberPerLine == 0:
            print()

printList('과학', 4, l)

print("{0:=^70}".format('Q.1'))

def avg():
    a = 0
    while a != -1:
        a = int(input('a :'))
        if a != -1:
            b = int(input('b :'))
            result = (a + b)/2
            print(a,'와',b,'의 평균은',result,'입니다')
        else:
            print('종료되었습니다')
avg()

print("{0:=^70}".format('Q.2'))

def make_list(list_name):
    a = 0
    list_name = []
    while a != -1:
        a = int(input('숫자를 입력하세요'))
        if a != -1:
            list_name.append(a)
        else:
            print('최댓값:', max(list_name), '최솟값:', min(list_name))
make_list('숫자')

print("{0:=^70}".format('Q.3'))


def sum_range():
    c = 0
    a = int(input('시작'))
    b = int(input('끝'))
    while a <= b:
        if a < b:
            c = c + a
            a = a + 1
        else:
            a = a + 1
            sum_total = c + b
            print(a, '에서부터', b, '까지의 합은', sum_total,'입니다.')
sum_range()

# for를 써서 실행해보기

print("{0:=^70}".format('Q.4'))

x = ['seoul', 'daegu', 'end', 'kwangju', 'jeju', 'end']


def str_3(str_list):
    a = len(str_list)
    c = []
    for k in str_list:
        b = k[0:3]
        if b != 'end':
            c.append(b)
        else:
            print('종료되었습니다')
    return c


def str_2():
    c = []
    a = 0
    while a != 'end':
        a = input('문자를 입력하세요')
        if a != 'end':
            c.append(a[0:3])
        else:
            print('종료되었습니다')
    return c

print("{0:=^70}".format('Q.5'))

def myrange(*inja):
    a = len(inja)
    if a == 1:
        b = range(inja[0])
        l = [ x for x in b]
    elif a == 2:
        c = range(inja[0], inja[1] + 1)
        l = [x for x in c]
    elif a == 3:
        d = range(inja[0], inja[1] + 1, inja[2])
        l = [x for x in d]
    else:
        print('Error')
    return tuple(l)

print(myrange(1, 100, 2))

print("{0:=^70}".format('Q.6'))

def operator():
    a = 0
    b = 0
    c = 0
    d = ['+', '-', '*', '/']
    while c != 'end':
        c = input('종료하시려면 "end", 계속하시려면 "pass"를 입력하세요.')
        if c != 'end':
            a = int(input('First Number:'))
            op_int = int(input('1.add, 2.subtract, 3.multiply, 4.divide'))
            op_d = d[op_int - 1]
            b = int(input('Second Number'))
            result = eval('a' + op_d + 'b')
            print(a, op_d, b, '=', result)
        else:
            print('Stop')

operator()

print("{0:=^70}".format('Q.7'))

def calcScore(sub_list):
    x = range(0, len(sub_list))
    a =[]
    b = 0
    total = 0
    Avg = 0
    grade = ['Excellent', 'Fail', ' ']
    while b != 'end':
        for k in x:
            if b != "end":
                a.append(int(input(sub_list[k] + '의 점수를 입력하세요')))
                total = total + a[k]
                b = input('종료하시려면 "end", 계속하시려면 "pass"를 입력하세요.')
                Avg = total / len(sub_list)
            else:
                if Avg >= 90:
                    result_g = total, Avg, grade[0]
                elif Avg <= 50:
                    result_g = total, Avg, grade[1]
                else:
                    result_g = total, Avg, grade[2]
    return tuple(result_g)

l = ['국어', '영어', '수학', '과학']
print(calcScore(l))


from collections import namedtuple
def inputStudentInfo():
    count_n = 0
    name = ' '
    number = namedtuple('점수', )