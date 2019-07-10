"""
클래스를 이용한 계산기 만들기
"""

# [1] Class 만들기
class FourCal:
    pass

a = FourCal()  # FourCal 클래스를 객체 a에 할당
print(type(a)) # 객체 a의 타입은 FourCal 클래스이다.

# [2] Class 데이터 요소/ 객체 만들기
class FourCal:                          # 여기서 'self'는 할당되는 객체 자체를 의미한다.
    def setdata(self, first, second):   # 클래스 안에 구현된 함수 = Method
        self.first = first              # 클래스 내부의 함수
        self.second = second

a = FourCal()
a.setdata(4, 2)
print('a의 첫번째 수', a.first, '/', 'a의 두번째 수', a.second)

# [3] 여러가지 객체 만들기
a = FourCal()
b = FourCal()
a.setdata(10, 2)
b.setdata(3, 8)

print(a.first, a.second, '\n',
      b.first, b.second)

# [4] 더하기, 빼기, 곱하기, 나누기 기능 만들기

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(10, 4)
print(a.add())

# [5] 생성자 만들기(Constructor)
#           생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미

# a = FourCal()
# print(a.add())
        # Traceback (most recent call last):
        #   File "<input>", line 3, in <module>
        #   File "<input>", line 7, in add
        # AttributeError: 'FourCal' object has no attribute 'first'
# 오류가 나오는 이유는 a객체의 setdata를 설정하지 않았기 때문이다.

'''
객체의 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출해 초깃값을
설정하기 보다는 생성자를 구현하는 것이 안전한 방법이다.
'''

# __init__ 을 사용해 초깃값을 설정

class FourCal:
    def __init__(self, first, second):  # __init__ 으로 생성자로 인식되어 객체가 생성되는 시점에서
        self.first = first              # 자동으로 호출된다.
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(19, 27)
print(a.first)
print(a.second)

print(a.add())
print(a.mul())

# [6] 클래스의 상속
#           상속을 하는 이유는 기존의 클래스를 변경하지 않고
#           기능을 추가하거나 수정할 때 사용한다. (library 같은 경우 수정이 불가능할 떄가 있다)
class MoreFourCal(FourCal): # class 클래스 이름(상속할 클래스 이름)
    pass

a = MoreFourCal(7, 9)
print(a.add())
print(a.mul())
print(a.sub())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(10, 4)
print(a.pow())


# [7] Method Overriding(일종의 덮어쓰기)

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(10, 0)
print(a.div())

# [8] 클래스 변수

class Family:
    lastname = "김"

print(Family.lastname)  # 김

a = Family()
b = Family()

print(a.lastname)   # 김
print(b.lastname)   # 김

Family.lastname = "박"

print(a.lastname)   # 박
print(b.lastname)   # 박

