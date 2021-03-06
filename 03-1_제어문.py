# 03-1_제어문
"""
제어문 :
2019-07-05
"""
# if, for, while


# if 문

a = 10
if a > 5 :
    print("Big")
else :
    print("Small")

if a == 10 :
    print("a = 10")

if a == 10 :
    print("a = 10")
else :
    pass


order = 'ham'
if order == 'spagetti' :
    Price = 5000
elif order == 'spam' :
    Price = 6000
elif order == 'egg' :
    Price = 7000
elif order == 'ham' :
    Price = 8000
else :
    Price = 0

print("Order price : %d" % Price)

if a > 5 :
    x = a * 2
else :
    x = a / 2
print(x)

x = a * 2 if a > 5 else a / 2   # a 가 5보다 크면 x는 a * 2
print(x)

a = 10
t = (a/2, a*2)
index = a > 5
x = t[index]
print(x)


a = 10                          # 실무형
x = (a/2, a*2)[a > 5]           # [] 는 지금 indexing - True = 1 or False = 0
print(x)                        # 튜플의 인덱스를 선택

a = 10
x = {False:'짝수', True:'홀수'}[a%2]
print(x)
# x = { 'a':1, 'b':2, 'c':3 }
# print(x[a]) : 1 값이 나온다

x = {False:'짝수', True:'홀수'}[a%2][0]
print(x)
x = {False:'짝수', True:'홀수'}[a%2][1]
print(x)
x = {False:'짝수', True:'홀수'}[a%2].strip('수')
print(x)                        # strip 에 '수'를 넣으면 '수'를 없애준다.

# for 문

for k in range(10):
    print(k)

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for k in l :
    print(k)

l = ['cat', 'dog', 'bird', 'pig', 'tiger']
for k in l:
    print(k)


l = ['cat', 'dog', 'bird', 'pig', 'tiger']
for i, k in enumerate(l) :
    print(i, k)                             # index 값과 같이 나타난다.
# 0 cat
# 1 dog
# 2 bird
# 3 pig
# 4 tiger

l = ['cat', 'dog', 'bird', 'pig', 'tiger']
for i, k in enumerate(l):             # enumerate : index 값도 반환
    print(i, k)
    if i == 3 :
        print('[3:%s]'%k)             # 3번째에는 다른 처리를 하고 싶은 경우

# continue, break문
for x in range(10):
    if x > 3 :
        break           # for 문 Loop를 탈출
    print(x)

print('-'*50)

for x in range(10):
    if x < 3 :
        continue        # continue는 사실상 skip과 비슷
    print(x)            # for문의 continue 다음 문장을 skip하고
                        # for문의 시작지점으로 돌아간다


l = ['cat', 'dog', 'bird', 'pig', 'tiger']
for x in l :
    if x == 'pig' :
        break
    print(x)

# 중첩된(nested)
for x in range(2,4):                        # 곱셈 9단까지
    for y in range(1,10):                   # 출력
        print(x, '*', y, '=', x*y )


# while 문
a = 0
while a < 10:
    print(a)
    a = a + 1

while True:
    print(a)
    a = 1+1

while True:
    print(a)
    a = a + 1
    if a == 1000: break

print('{0:-^70}'.format('제어문 실습과제'))
print('{0:-^70}'.format('Q1'))
# 1
for x in range(1, 101) :
    print(x, end=' ')
    if x % 10 == 0:
        print(x, end = '\n')

#2
a = [[x+((t-1)*10) for x in range(1, 11)] for t in range(1, 11)]
print(a)

print('{0:-^70}'.format('Q2'))

n = int(input('n ='))
total = 0

for x in range(1, n+1) :
    print(x)
    total = total + x

print('총합', total)

print('{0:-^70}'.format('Q3'))
n = int(input('n = '))
total_odd = 0
total_even = 0

for x in range(1, n + 1):
    if x % 2 == 0:
        print(x)
        total_even = total_even + x
    else:
        print(x)
        total_odd = total_odd + x
print('짝수:', total_even, '홀수:', total_odd)

print('{0:-^70}'.format('Q4'))
n = int(input('n = '))
total = 0
for x in range(1, n + 1):
    if x % 3 == 0:
        pass
    elif x % 5 == 0:
        pass
    else:
        print(x)
        total = total + x
print('총합', total)

print('{0:-^70}'.format('Q5'))
#1
for x in range(2, 10):
    for y in range(1, 10):
        print(x, '*', y, '=', x*y)
#2
a = [2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in a:
    for y in b:
        print(x, '*', y, '=', x * y)

z = [[x * i for x in range(1,10)] for i in range(2,10)]
print(z)

print('{0:-^70}'.format('Q6'))

a = 0

plu = 0
plu_odd = 0
plu_even = 0
min = 0

while a != -999:
    a = int(input('NUMBER'))
    if a > 0:
        plu = plu + 1
        if a % 2 == 0:
            plu_even = plu_even + 1
        else:
            plu_odd = plu_odd + 1
    elif a < 0:
        min = min + 1
    else:
        pass
print('양수:', plu, '음수', min, '양수-짝수:', plu_even, '양수-홀수:', plu_odd)

print('{0:-^70}'.format('Q7'))

operator = {1:'+', 2:'-', 3:'*', 4:'/'}
a = int(input('NUM_1'))
x = int(input('연산자를 입력하세요 [1:+, 2:-, 3:*, 4:/]'))
b = int(input('NUM_2'))
operator_n = operator[x]

result = eval('a' + operator_n + 'b')
print(a, operator_n, b, "=", result)

print('{0:-^70}'.format('Q8'))

from collections import namedtuple
number = namedtuple('점수', '점수_1, 점수_2, 점수_3')

count_n = 0

name = ' '

while (count_n < 10):
    name = input('이름을 입력하세요.')
    if name == 'end':
        break
    else:
        pass
    a = int(input('점수_1'))
    b = int(input('점수_2'))
    c = int(input('점수_3'))
    count_n = count_n + 1
    name1 = name                                # name1에 name을 복사/할당
    name1 = number(a, b, c)
    avg = (name1.점수_1 + name1.점수_2 + name1.점수_3)/3
    if avg >= 90 :
        print('이름:', name, '\n', '점수_1:', name1.점수_1,
              '점수_2:', name1.점수_2, '점수_3:', name1.점수_3, '\n',
              '총점:', name1.점수_1 + name1.점수_2 + name1.점수_3,
              '평균:', avg, 'Excellent')
    elif avg <= 50:
        print('이름:', name, '\n', '점수_1:', name1.점수_1,
              '점수_2:', name1.점수_2, '점수_3:', name1.점수_3, '\n',
              '총점:', name1.점수_1 + name1.점수_2 + name1.점수_3,
              '평균:', avg, 'Fail')
    else:
        pass

