# 05-2_클래스상속.py

# 상위 클래스 - 부모 클래스
class Calculator():

    def __init__(self):
        print('Calculator 생성자: 상위클래스')
        self.a_range = 20000
        self.b_range = 1000

    def add(self, a, b):
        if a > self.a_range or b > self.b_range:
            return 'Over Range!!'
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        print("상위클래스 divide")
        return a / b

# cal = Calculator()
# print(cal.add(10, 20))
# print(cal.divide(20, 10))
# print(cal.divide(20, 0))    ZeroDivisionError: division by zero

# 하위 클래스 - 자식 클래스 - 파생 클래스
# 상속 : class 자식클래스(부모클래스1, 부모클래스2, 부모클래스3, ...)
class More_Calculator(Calculator):

    def __init__(self):
        print('Calculator 생성자: 하위클래스')
        Calculator.__init__(self)           # 부모 클래스의 생성자를 호출

    # 추가 Method 를 구현

    def pow(self, a , b):
        return a ** b

    def add_3(self, a, b, c):
        return a + b + c

    # Method Overriding : 상속
    # 부모클래스의 Method를 자식 클래스가 재정의하여 새롭게 Method를 구현
    def divide(self, a, b):
        print("하위클래스 divide")   # 상위클래스보다 하위클래스 divide가 우선 실행된다.
        if b == 0:
            return ' zero Divide!!'

        return a/b




# mcal = More_Calculator()
# print(mcal.pow(11, 20))
# print(mcal.divide(10, 0))
# print(mcal.divide(10, 2))
#
# mcal.a_range = 30000
# mcal.b_range = 2000
# print(mcal.add(20001, 1001))


#------------------------------------------------------------------------------------------------

import Car_class as car

class Airplane(car.Car):

    def __init__(self):
        self.air_name = 'KAL147'
        self.air_height = 0
        self.air_speed = 0
        self.air_direction = '정지'
        self.air_state = '정상'

    def set_air_name(self, air_name):
        self.air_name = air_name
        print('{0}[{1}]{2}'.format("비행기 기종이 ", air_name, "로 변경 되었습니다"))

    def get_air_name(self):
        return self.air_name

    def set_height(self, height):
        self.height = height
        print('{0}[{1}]{2}'.format("비행 고도를", height, "km 로 설정하였습니다."))

    def get_height(self):
        return self.height

    def land_to_ground(self):
        self.air_direction = '착륙'
        print('비행기가 착륙하였습니다.')
        return self.air_direction

    def set_speed(self, speed):
        self.air_speed = speed
        print('{0}[{1}]{2}'.format("비행기의 속력이 시속 ", speed, "km로 변경되었습니다."))

    def get_speed(self):
        return self.air_speed

    def move_forward(self):
        self.air_direction = "앞쪽"
        print('{0}[{1}]{2}'.format("비행기가 전진합니다. 속도는 ", self.air_speed, "km 입니다." ))
        return self.air_direction

    def move_backward(self):
        self.air_direction = "뒤쪽"
        print('{0}[{1}]{2}'.format("비행기가 후진합니다. 속도는 ", self.air_speed, "km 입니다." ))
        return self.air_direction


air = Airplane()
air.set_air_name('아시아나104')
print(air.get_air_name())
air.set_height(1000)
print(air.get_height())
air.land_to_ground()
air.set_speed(100)
print(air.get_speed())
air.move_forward()
air.move_backward()

