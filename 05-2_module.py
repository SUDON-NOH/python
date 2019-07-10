# 05-2_모듈
"""
Module : 모듈
main Module
2019-07-09
"""
# import calculator
#
# # calculator 를 import 하는 순간 calculator 전체가
# # 복사된 상태로 현 페이지로 붙여넣기 된다.
#
#
# result = calculator.add(100,200)
# print(result)
#
# print(__name__) # 최상위에 있는 소스를 main 모듈이라고 한다.

# import calculator as cal
# if __name__ == '__main__':
#     result = cal.add(100, 200)
#     print(result)
#
#     result = cal.sub(100, 200)
#     print(result)
#
#     result = cal.mul(100, 200)
#     print(result)
#
#     result = cal.div(100, 200)
#     print(result)


from calculator import add  # 한가지 함수만 호출
from calculator import add, sub  # 두가지 함수만 호출
from calculator import *  # 모든 함수 호출
if __name__ == '__main__':
    result = add(100, 200)
    print(result)

    result = sub(100, 200)
    print(result)

    result = mul(100, 200)
    print(result)

    result = div(100, 200)
    print(result)


