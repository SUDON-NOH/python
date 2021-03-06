# 02-3_리스트
"""
리스트 자료형 : mutable 자료형, 시퀀스
2019-07-02
"""

# list에 쓰이는 괄호 : []

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(type(a))                  # <class 'list'>


# indexing

print(a[0], a[1], a[2], a[3], a[8])
print(a[-1], a[-2], a[-3], a[-6])

a[0] = 10                      # mutable 자료형이기 떄문에
print(a)                       # 요소의 변경이 가능하다
a[0] = 1
print(a)


# slicing

print(a[1:3])


a[1:5] = [20, 30, 40, 50]
print(a)
a[1:5] = [2, 3, 4, 5]

# a[시작옵셋:(끝옵셋 +1): 간격(step)]
print(a[0 : 8 : 2])           # 홀수만 출력
print(a[:: -1])               # 거꾸로 출력 [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[8::-1])               # [9, 8, 7, 6, 5, 4, 3, 2, 1]

a[::2] = [10, 30, 50, 70, 90] # 홀수만 출력
print(a)

# range 함수 용법

list_1 = list(range(1, 10))    # 1부터 9까지 출력
print(list_1)

list_1_2 = list(range(10))    # 0부터 9까지 출력
print(list_1_2)

list_2 = list(range(1,100,2)) # 1부터 99까지 홀수만 출력
print(list_2)

# sum() 함수 : 시퀀스형 데이터의 총합을 구한다.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(a))
print(max(a))
print(min(a))

print('{0:=^70}'.format('실습과제'))
print('{0:=^70}'.format('Q.1'))

list = ['+', '-', '*', '/']
a = input( 'a = ')
b = input( 'b = ')
op_select = int(input('input operator( 1:+, 2:-, 3:*, 4:/) : '))
op = list[op_select - 1]

result = eval(a + op + b)
print(result)


print('{0:=^70}'.format('Q.2'))
a = int(input(' n = '))
list_a = range(1, a + 1)


sum_total = sum(range(1, a + 1))
print(sum_total)

print('{0:=^70}'.format('Q.3'))
a = int(input(' n = '))
list_b = range(1, a + 1)

sum_odd = sum(list_b[::2])
sum_even = sum(list_b[1::2])

print(sum_odd)
print(sum_even)

print('{0:=^70}'.format('Q.4'))

a = int(input(' n = '))
list_c = range(1, a + 1)

sum_e35 = sum(list_c) - sum(list_c[2::3]) - sum(list_c[4::5])
print(sum_e35)


print('{0:=^70}'.format('if문 연습'))
pocket = ['print', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고가라')
else:
    print('걸어가라')



op_select = int(input('What do you have ? ( 1:bus card, 2:money, 3:cellphone, 4:Nothing)'))
list_a = ['bus card', 'money', 'cellphone', 'Nothing']
OP = list_a[op_select - 1]

if OP == 'bus card' :
    print('버스를 타라')
elif OP == 'money' :
    print('택시를 타라')
elif OP == 'cellphone' :
    print('엄마한테 전화해라')
else:
    print('걸어가라')
print('{0:=^70}'.format('if문 연습'))