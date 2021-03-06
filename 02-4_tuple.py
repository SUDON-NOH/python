# 02-4_튜플
"""
튜플 자료형 : immutable 자료형, 순서형(sequence)
2019-07-03
"""

a = (1, 2, 3, 4, 5, 6, 7)
print(a, type(a))        # (1, 2, 3, 4, 5, 6, 7) <class 'tuple'>

# indexing
print(a[0], a[1], a[2], a[3])
print(a[-1], a[-2], a[-3], a[-4])

# a[0] = 10           # TypeError : 요소값 변경이 불가
                      # 요소값을 변경하려면 새로운 객체를 만들어야 한다

b = list(a)           # 튜플로 바꾸려면 먼저 a를 리스트로 변경하고
b[0] = 10             # 넣고 싶은 값을 넣고
b = tuple(b)          # 다시 튜플로 돌려놓는다
print(b, type(b))     # 끝!


b = list(a)
b[0] = [1, 2, 3]
b = tuple(b)
print(b, type(b))

b[0][0] = 2
print(b, type(b))

# slicing
print(a[0:2])
print(a[::2])
print(a[::-1])
# a[::2] = (10, 30, 50, 70) # TypeError, 요소값 변경이 불가


# Packing / Unpacking

t = 1, 2, 3
print(t, type(t))   # (1, 2, 3) <class 'tuple'>


a, b, c = 10, 20, 30        # 모습은 튜플이지만 변수를 여러개 만들어
print(a, type(a))           # int형으로 받는다.


# a = [1, 2, 3, 4, 5]       # list 중 tuple형이 있을 경우에도
# a[0] = 1, 2, 3            # tuple의 요소를 변경할 수 없다
# a[0][2] = 3
# print(a)

t = 1, 2, 'hello' # <class 'tuple'> # Packing(tuple)
x, y, z = t                         # Unpacking(tuple)
print(x,y,z,type(x),type(y),type(z))

l = ['foo', 'bar', 4, 5]    # Packing(list)
x, y, z, w = l              # Unpacking(list)
print(x, y, z, w, type(x), type(y), type(z), type(w))

# 확장된 unpkacing 방법
t = (1, 2, 3, 4, 5)               # ValueError: too many values to unpack (expected 2)
# a, b = t                        # 꺼내려고 하는데 객체의 수가 너무 적음
a, *b = t
print(a, b)                 # a = 1             # *가 나머지 전체라는 뜻
                            # b = [2, 3, 4, 5]

*a, b = t                   # a = [1, 2, 3, 4]
print(a, b)                 # b = 5

t = 1, 2, 'hello'
x, y, _ = t
print(x, y, _, type(x), type(y), type(_))

t = () # 빈 튜플
t = 1, 2, 3
t = 1
print(type(t))      # <class 'int'>
t = (1, )
t = 1,              # 데이터가 1개라도 쉼표를 사용하면 tuple
print(t, type(t))   # (1,) <class 'tuple'>

# 연산자
t1 = (1, 2, 3)
t2 = ('apple', 'banana')
t3 = t1 + t2        # 합 연산 t3 = t1.__add__(t2)와 동일결과
print(t3)           # (1, 2, 3, 'apple', 'banana')
print(t1.__add__(t2))

t4 = t1 * 2         # 반복연산
print(t4)           # (1, 2, 3, 1, 2, 3)

print(len(t4))      # 요소의 수
print(1 in t1)      # True
print(sum(t1))      # 연속 자료형 데이터들의 총합
print(min(t1))
print(max(t1))

t = (1, 2, 3, 2, 2, 3)
print(t.count(2))       # 3, 2 값을 갖는 요소의 개수
print(t.index(2))       # 1, index
print(t.index(2,2))     # 3, index
print(t.index(2,4))     # 4, index 4번째부터 2를 찾는 데 2가 4번째에 있어서 결과 값이 4


# tuple 중첩
t = (12345, 54321, 'hello')
u = t, (1, 2, 3, 4, 5)
print(u)
print(u[0][2])
print(u[0][2][1])

# 두 개의 값을 서로 변경

x, y = 1, 2
# temp = x
# x = y
# y = temp
x, y = y, x
print(x, y)
(x1, y1),(x2, y2) = (1, 2),(3, 4)   # 복수개의 변수값을
print(x1,y1,x2,y2)                  # 할당가능


print('{0:=^70}'.format('실습과제'))
a = ('a1', 'a2', 'a3', 'a4')
b = ('b1', 'b2', 'b3', 'b4')
print('{0:=^70}'.format('Q.1'))
q, w, e, r = a[0], a[1], a[2], a[3]
print(q,w,e,r)
print('{0:=^70}'.format('Q.2'))
c = a + b
print('a + b = c :' , c)
print('a + b = c :' , a.__add__(b))
print('{0:=^70}'.format('Q.3'))
print('{0}{1}'.format("c의 3번째 자리 = ", c[2]))
print('{0:=^70}'.format('Q.4'))
print('c의 6번째 부터 끝까지', c[5:])
print('{0:=^70}'.format('Q.5'))
print('c의 처음부터 3번째까지', c[:4])
print('{0:=^70}'.format('Q.6'))
c.remove(c[3])
print('{0:=^70}'.format('Q.7'))
c[5] = 'c1'


# named tuple : 이름있는 튜플 : 함수의 좌표와 유사
# 튜플을 숫자 인덱스가 아닌 이름으로 접근 가능하다
from collections import namedtuple
point = namedtuple('dot','x, y')     # 이름이 있는 튜플의 class' instance(객체)를 생성
print(point.__name__)                # 이름을 출력
pt1 = point(1.0, 5.0)
pt2 = point(2,3)
pt3 = point('Hello', 'Good bye')
print(pt1, pt2, pt3)
# dot(x=1.0, y=5.0) dot(x=2, y=3) dot(x='Hello', y='Good bye')
print(type(print))
number = pt1.x + pt1.y
print(number, type(number))         # 6.0 <class 'float'>
string = pt3.x + ' ' + pt3.y
print(string, type(string))         # Hello Good bye <class 'str'>
