# 05-1_Class
"""
클래스
2019-07-10
"""

#   1. 파이썬 클래스 관련 용어
#     [1] 클래스(Class)        - 과자를 만들 때 사용하는 틀
#       (1) Class 문으로 정의하며, member와 method를 가지는 객체
#       (2) 새로운 이름 공간을 갖는 단위
#       (3) 속성을 갖고 있어야 클래스가 된다.
#       (4) 대부분 대문자로 시작
#
#     [2] 클래스 객체(Class Objcet) : 클래스와 같은 의미
#
#     [3] 클래스 인스턴스(Class Instance)      - 과자
#       (1) 클래스를 호출하여 생성된 객체
#
#     [4] 클래스 인스턴스 객체(Class Instance Object) : 클래스 인스턴스와 같은 의미
#       (1) 인스턴스 객체라고 부르기도 한다.
#
#     [5] Member (멤버) : 클래스 혹은 클래스 인스턴스 공간에 정의된 "변수"
#     [6] Method (메서드) : 클래스 공간에 정의된 "함수", def로 정의
#     [7] 속성(Attribue) : Class + method 전체를 가리킨다.
#     [8] 상속(Inheritance) : 상위 클래스의 속성과 행동을 그대로 받아들이고,
#                            추가로 필요한 기능을 덧붙이는 것

# 클래스와 인스턴스 객체
# class "클래스 이름":
#   속성 ...
class Simple:   # 클래스
    pass
print(Simple)   # <class '__main__.Simple'>

s1 = Simple()   # 클래스의 인스턴스 객체
print(type(s1), s1) # <class '__main__.Simple'> <__main__.Simple object at 0x000002247EA60208>

s2 = Simple()   # 클래스의 인스턴스 객체
print(type(s2), s2) # <class '__main__.Simple'> <__main__.Simple object at 0x000002247EA60390>

del s1          # 객체의 삭제 , 파이썬에서는 직접 삭제할 필요는 없다.
print(s1)       # NameError: name 's1' is not defined

# 멤버 접근 : 클래스 멤버와 인스턴스 멤버
# (1) 클래스 멤버의 구현과 접근 방법
class MyClass:
    cl_mem = 100    # 클래스 멤버
    cl_list = []    # 클래스 멤버
    a = 'Hi'
# 클래스 객체를 통해서 접근
print(MyClass.cl_mem)       # 100   # 클래스 멤버를 읽어오기
print(MyClass.cl_list)      # []
print(MyClass.a)            # Hi
MyClass.cl_mem = 200                # 클래스 멤버를 변경하기
print(MyClass.cl_mem)       # 200

MyClass.a = 'bye'
print(MyClass.a)            # bye

MyClass.cl_list = [4, 5, 6]
print(MyClass.cl_list)      # [4, 5, 6]

print('-'*50)

# 클래스의 인스턴스 객체를 통해서 접근
# 인스턴스 객체를 통해 변경하면 인스턴스의 값만 변경된다.
# 원본 클래스는 변경되지 않는다.

m1 = MyClass()     # 클래스의 인스턴스 객체
print(m1.cl_mem)   # 200
print(m1.a)        # bye
print(m1.cl_list)  # [4, 5, 6]

m1.cl_mem = 300                 # 이와 같이 객체를 변경하였을 때,
print(m1.cl_mem)        # 300   # 복사본인 객체만 변경된다
print(MyClass.cl_mem)   # 200   # 원본이 변경되지 않는다.


# (2) 인스턴스 멤버의 구현과 접근 방법
class MyClass2():
    
