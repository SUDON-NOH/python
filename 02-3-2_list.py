# 02-3_리스트
"""
리스트 자료형 : mutable 자료형, 순서형(sequence)
2019-07-03
"""

# LIST 연산
a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
print(c)        # [1, 2, 3, 3, 4, 5]
d = a * 3
print(d)        # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(len(a)) # 3

# List 에 객체 존재 유무 묻기
print(3 in a) # True
print(0 in a) # False

# del : 객체를 삭제
del b[0]
print(b)

# append : List 에 객체를 추가
a.append(4)
print(a)         # [1, 2, 3, 4]

a.append([5, 6]) # list 를 추가 가능 # [1, 2, 3, 4, [5, 6]]
print(a)         # 리스트를 추가 할 때는 + 를 사용

# insert : List  원하는 위치에 객체를 추가
a.insert(1, 1.5) # insert(index, data)
print(a)

# remove : List 에서 제거하고 싶은 객체를 제거
a.remove(1.5)
print(a)
a.remove([5,6])
print(a)

# pop : 어떤 stack(순차적으로 쌓이는 데이터) 에서 데이터를 제거
# 리스트의 마지막 요소를 제거
a.pop()
print(a)    # [1, 2, 3]

# 정렬
a = [1, 6, 2, 4, 3, 3, 7, 8]
a.sort()                # 정렬
print(a)                # [1, 2, 3, 3, 4, 6, 7, 8]
a.sort(reverse = True)  # [8, 7, 6, 4, 3, 3, 2, 1] # 역순 정렬
print(a)
a.reverse()             # 순서를 반대로
print(a)                # [1, 2, 3, 3, 4, 6, 7, 8]

# index : 값의 위치를 찾는다
print(a.index(3))       # 2
# print(a.index(9)  )   # ValueError: 9 is not in list

# count : 값의 개수를 센다
a.append(3)
print(a.count(3))

# extend : 리스트 확장
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# 확장 슬라이싱 : 시작과 끝값이 없고 step값 만 인정
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(c[::2])   # [0, 2, 4, 6, 8, 10]

# 중첩(nested)리스트 : list 안에 list 가 존재
a = [1, 2, 3, 4, [5, 6, 7]]         # 2중 리스트
print(a[4])
print(a[4][1])                      # a의 index 4번에 index 1번

a = [1, 2, 3, 4, [5, 6, 7, [8, 9, 10]]]    # 3중 리스트
print(a[4])                                # [5, 6, 7, [8, 9, 10]]
print(a[4][3])                             # [8, 9, 10]
print(a[4][3][1])                          # 9

a = [7, 8, 9]
b = [4, 5, 6, a]                    # 2중 리스트
c = [1, 2, 3, b]                    # 3중 리스트
print(b)                            # [4, 5, 6, [7, 8, 9]]
print(c)                            # [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
# a = [10, 11, 12]                  # a 객체를 바꿨을 때, b , c 를 프린트 하면
                                    # 원래 있던 a가 출력된다.
# print(b)                          # [4, 5, 6, [7, 8, 9]]
# print(c)                          # [1, 2, 3, [4, 5, 6, [7, 8, 9]]]

a[0] = 10                           # a 의 요소를 바꾸면 바뀐 a 가 출력된다.
print(b)                            # [4, 5, 6, [10, 8, 9]]
print(c)                            # [1, 2, 3, [4, 5, 6, [10, 8, 9]]]


# List Comprehension : 리스트 내장
# <식> for <타깃1> in <객체1>
#     ...
#     for <타깃n> in <객체n>

a = [k for k in range(10)]
print(a)

a = [1, 2, 3, 4, 5, 6, 7]
b = [k for k in a if k > 4]         # [5, 6, 7]
print(b)
c = [k for k in a if k % 3 == 0]    # 3의 배수
print(c)
d = [k for k in a if k % 3 != 0]    # 3의 배수가 아닌 것
print(d)
e = [k for k in a if k % 3 != 0 and k % 2 != 0]    # 3의 배수가 아니고 2의 배수가 아닌 것
print(e)

# 리스트 내장을 이용한 데이터의 조합 리스트 생성
seq1 = 'abc'            # 문자열
seq2 = (1, 2, 3)        # 튜플

l = [(x, y) for x in seq1 for y in seq2]
print(l)
# [('a', 1), ('a', 2), ('a', 3),
# ('b', 1), ('b', 2), ('b', 3),
# ('c', 1), ('c', 2), ('c', 3)]

l = [ (seq1 , y) for y in seq2]
print(l)

# for 문

for k in range(0, 10) :
    print(k, end = ',')

total = 0
# for m in range(11)     : # From 0 to 10 , step = 1
# for m in range(1, 11)  : # from 1 to 10 , step = 1
# for m in range(1,11,2) : # from 0 to 10 , step = 2

for k in range(0, 11, 2) :          # shift + f9
    print(k)                        # f8
    total = total + k               # breakpoint
print('total:', total)

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0], a[2], a[4], a[6], a[8])
print(a[::2])                       # list를 슬라이싱

for k in range(9):
    print(a[k], end = ' ')

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for k in range(0, 9, 2):
    print(a[k], end = ',')

print('{0:=^70}'.format('실습과제'))
print('{0:=^70}'.format('Q.3'))

num = int(input('n ='))
a = [k for k in range(num + 1)]

odd = sum([odd for odd in a if odd % 2 == 0])
even = sum([even for even in a if even % 2 != 0])
print(odd)
print(even)

print('{0:=^70}'.format('Q.4'))

max_number = int( input( 'Input max number : ' ) )
l = [ x for x in range( 1, max_number + 1 ) if x % 3 != 0 and x % 5 != 0 ]

print(l)



print('{0:=^70}'.format('Teacher\'s'))

# 3번 답안
print( '{0:=^50}'.format( '3' ) )
max_number = int( input( 'Input max number : ' ) )

even = list( range( 2, max_number + 1, 2 ) )
odd = list( range( 1, max_number + 1, 2 ) )

print()
print( 'even number : ', even )
print( '1 ~ {0:^6} = {1:<8}\n'.format( max_number, sum( even ) ) )

print( 'odd number : ', odd )
print( '1 ~ {0:^6} = {1:<8}'.format( max_number, sum( odd ) ) )

# 4번 답안
print( '{0:=^50}'.format( '4' ) )
max_number = int( input( 'Input max number : ' ) )

l3 = [ x for x in range( 1, max_number + 1 ) if x % 3 == 0 ]
l5 = [ x for x in range( 1, max_number + 1 ) if x % 5 == 0 ]
l = [ x for x in range( 1, max_number + 1 ) if x % 3 != 0 and x % 5 != 0 ]

print(l)

print( 'Multiple of 3 : ', l3, '\n' )
print( 'Multiple of 5 : ', l5, '\n' )
print( 'Excluding Multiple of 3 and 5 : ', l )
print( 'sum = {0:<6}'.format( sum( l ) ) )

