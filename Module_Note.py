"""
모듈 module
"""

# [1] Module이란?
#       함수나 변수 또는 클래스를 모아 놓은 파일
#       다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일

# [2] 모듈 만들기
#       파이썬 파일 mod1.py 에 add 와 sub 함수를 정의해 놓는다.
#
#      mod1.py
#               def add(a, b):
#                    return a + b
#
#               def sub(a, b):
#                    return a - b

# [3] 모듈 불러오기

import mod1                 # mod1 모듈 불러오기
print(mod1.add(3,4))
print(mod1.sub(4,2))

from mod1 import add        # mod1 모듈에서 add 함수만 불러오기
print(add(3, 4))
print(add(1, 2))

from mod1 import sub        # mod1 모듈에서 sub 함수만 불러오기
print(sub(2, 1))
print(sub(5, 1))

from mod1 import add, sub   # mod1 모듈에서 sub 함수와 add 함수 같이 불러오기
print(sub(2, 1))
print(add(3, 4))

from mod1 import *          # mod1 모듈에서 모든 함수 불러오기
print(sub(2, 1))
print(add(3, 4))

# [4] if__name__=="__main__" 의 의미
# mod1.py 파일을 변경
# mod1.py 수정 전
#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b

# mod1.py 수정 후
#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# print(add(1, 4))
# print(sub(4, 2))

import mod1
print(sub(10, 5))
print(add(10, 5))
# if__name__=="__main__" 이 없는 경우
# 아래와 같이 출력된다.
"""
sub is called
1
add is called
7
sub is called
1
add is called
7
sub is called
5
add is called
15
"""

# __name__ 변수란?
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름
# 파이썬 셸이나 파이썬 모듈에서 mod1을 import 하는 경우에는 mod1.py의
# __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
# 따라서 if 문은 false가 되어 작동하지 않는다.

