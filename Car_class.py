class Car:

    def __init__(self):
        print('생성자')
        self.car_name = '소나타'
        self.car_drv = '전륜'
        self.car_speed = 0
        self.car_direction = '앞쪽'
        self.car_fuel = '휘발유'
        self.car_state = '정상'

    def set_car_name(self, name):
        self.car_name = name
        print("차종이 [",self.car_name,"]으로 변경 되었습니다")

    def get_car_name(self):
        return self.car_name

    def set_car_drv(self, drv):
        self.car_drv = drv
        print("차의 구동 방식이 [", self.car_drv ,"]으로 변경 되었습니다")

    def get_car_drv(self):
        return self.car_drv

    def set_car_fuel(self, fuel):
        self.car_fuel = fuel
        print("차의 연료 방식이 [", self.car_fuel,"]로 변경 되었습니다")

    def get_car_fuel(self):
        return self.car_fuel

    def set_car_state(self,state):
        self.car_state = state
        print("차의 상태가 [",self.car_state, "]으로 변경 되었습니다")

    def get_car_state(self):
        return self.car_state

    def set_speed(self,speed):
        self.car_speed = speed
        print("자동차의 속력이 시속 [",self.car_speed,"]km 로 변경되었습니다")

    def get_speed(self):
        return self.car_speed

    def turn(self,direction):
        self.car_direction = direction
        print("자동차의 방향이 [",self.car_direction ,"]으로 변경되었습니다")

    def stop(self):
        self.car_direction = '정지'
        print("자동차가 정지 하였습니다")

    def start(self):
        print("자동차가 시동이 걸렸습니다")

    def move_forward(self):
        self.car_direction = '앞쪽'
        print("자동차가 전진합니다 속도는 ",self.car_speed,"km입니다")

    def move_backward(self):
        self.car_direction = '뒤쪽'
        print("자동차가 후진합니다 속도는 ",self.car_speed,"km입니다")