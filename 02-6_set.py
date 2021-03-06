# 02-6_집합
"""
SET
2019-07-04
"""
# { }
# mutable 자료형
# 순서가 없다
# 중복을 허용하지 않는다.
# 중복 값을 제거하는데 이용 가능
s = {1, 2, 3}
print(s, type(s))               # {1, 2, 3} <class 'set'>

s = {3, 2, 1}
print(s, type(s))               # {1, 2, 3} <class 'set'>

l = [1, 2, 2, 3, 3, 4, 4, 5]    # 중복허용
print(l)                        # [1, 2, 2, 3, 3, 4, 4, 5]

s = {1, 2, 2, 3, 3, 4, 4, 5}    # 중복허용하지 않음
print(s)                        # {1, 2, 3, 4, 5}

print(len(l))                   # 8
print(len(s))                   # 5


# 연산자

s.add(6)                        # 집합에 1개의 요소 추가
print(s)

s.update({7,8,9})               # 집합에 여러개의 요소를 추가
print(s)

s.remove(9)                     # 원하는 데이터를 직접 입력
                                # 'del'은 위치를 입력 해야하지만 집합은 위치를 알 수 없음

# 집합의 연선 : 합집합, 교집합, 차집합, 대칭 차집합
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9, 10}

# 합집합 : '|', union()
s = s1 | s2
print(s)

s = s1.union(s2)
print(s)

# 교집합 : '&', intersection()
s = s1 & s2
print(s)

# 차집합 : '-', difference()
s = s1 - s2
print(s)

s = s1.difference(s2)
print(s)

# 대칭차집합 : (A-B)U(B-A)
s = s1.symmetric_difference(s2)
print(s)        # {1, 2, 3, 4, 7, 8, 9, 10}

s = (s1 - s2) | (s2 - s1)
print(s)        # {1, 2, 3, 4, 7, 8, 9, 10}


# 집합실습
# Q.1
a = [1, 2, 3, 4]
b = "aabbccddeeff"
s1 = set(a)
s2 = set(b)
print(s1, s2)

# Q.2
d = {'a', 'b', 'c'}
s1.update(d)
print(s1)

# Q.3
e = {1, 2}
s2.update(e)
print(s2)

# Q.4
s = s1 & s2
print(s)
s = s1.intersection(s2)
print(s)

# Q.5
s = s1 | s2
print(s)
s = s1.union(s2)
print(s)

# Q.6
s = s1 - s2
print(s)
s = s1.difference(s2)
print(s)

# Q.7
s = s2 - s1
print(s)
s = s2.difference(s1)
print(s)

# Q.8
s2.remove(1)
print(s)

# Q.9
s = s1.symmetric_difference(s2)
print(s)