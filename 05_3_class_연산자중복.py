# 05-2_클래스 연산자 중복.py

# 연산자 중복(Operator Overloading)
# 파이썬에 내장되어 있는 method(함수, 연산자)를
# 사용자 클래스 내에서 재정의하여 사용

class Calculator:
    def __init__(self):
        print('Calculator 생성자')
        self.a = 20
        self.b = 30
        self.info_str = 'Calculator class v1.0'

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def __add__(self, instance2):
        result1 = abs(self.a) + abs(instance2.b) # 절대값
        result2 = str(self.a) + str(instance2.b)
        print('연산자 중복:__add__')
        return result2, result1

# __str__은 __repr__ method를 대신할 수 없다.
    def __str__(self):
        print('연산자 중복:__str__')
        return self.info_str

# __repr__는 __str__ method를 대신할 수 있다.
    def __repr__(self):                 # class 를 문자열로 변환하는 데 많이 사용
        print('연산자 중복:__repr__')
        return self.info_str


cal = Calculator()          # 이미 __add__ 라는 내장 함수가 존재하지만
cal2 = Calculator()         # 직접 __add__ 라는 함수를 만들어서 적용
cal.a = 300                 # "+" 연산자를 method가 대체한다.
cal2.b = 500                # add 연사자뿐 아니라 수많은 것들이 존재
# print(cal.add(10, 20))
result = cal + cal2
print(result)

print(str(cal))             # __str__을 따로 지정하지 않으면
                            # class instance를 string 으로 변환하려 해도 적용이 되지 않음

print(repr(cal))

# # <Class int>
# a = 20
# b = 30
# c = a.__add__(b)        # "+"  =  __add__()
# print(c)
#
# # <Class str>
# a = 'Hi'
# b = 'Bye'
# c = a.__add__(b)
# print(c)


