class Car:

    def __init__(self,
                 name = 'sonata',
                 drv = '전륜',
                 speed = 0,
                 direction = '앞쪽',
                 fuel = '휘발유',
                 state = '정상'):

        print('생성자 호출')
        self.car_name = name
        self.car_drv = drv
        self.car_speed = speed
        self.car_direction = direction
        self.car_fuel = fuel
        self.car_state = state

    def set_car_name(self, name):
        self.car_name = name
        print('{0} [{1}]{2}'.format("차종이", name, "으(로) 변경 되었습니다"))

    def get_car_name(self):
        return self.car_name

    def set_car_drv(self, drv):
        self.car_drv = drv
        print('{0} [{1}]{2}'.format("차의 구동 방식이", drv, "으(로) 변경 되었습니다"))

    def get_car_drv(self):
        return self.car_drv

    def set_car_fuel(self, fuel):
        self.car_fuel = fuel
        print('{0} [{1}]{2}'.format("차의 연료 방식이", fuel, "으(로) 변경 되었습니다"))

    def get_car_fuel(self):
        return self.car_fuel

    def set_car_state(self, state):
        self.car_state = state
        print('{0} [{1}]{2}'.format("차의 상태가", state, "으(로) 변경 되었습니다"))

    def get_car_state(self):
        return self.car_state

    def set_car_speed(self, speed):
        self.car_speed = speed
        print('{0} [{1}]{2}'.format("차의 속력이 시속", speed, "km 로 변경 되었습니다"))

    def get_car_speed(self):
        return self.car_speed

    def turn(self, direction):
        self.car_direction = direction
        print("자동차의 방향이 ", direction, "으로 변경되었습니다.")

    def stop(self):
        self.car_direction = '[ 정지 ]'
        print("자동차가 정지 하였습니다.")
        return self.car_direction

    def start(self):
        self.car_direction = '[ 시동 ]'
        print("자동차가 시동이 걸렸습니다.")

    def move_forward(self, speed):
        self.car_speed = speed
        self.car_direction = '앞쪽'
        direction = '전진'
        print('{0} [{1}]{2} [{3}]{4}'.format("자동차가", direction, "합니다. 속도는", speed, "km 입니다."))

    def move_backward(self, speed):
        self.car_speed = speed
        self.car_direction = '뒤쪽'
        direction = '후진'
        print('{0} [{1}]{2} [{3}]{4}'.format("자동차가", direction, "합니다. 속도는", speed, "km 입니다."))

    def __del__(self):
        print(self.car_name, '자동차가 제거되었습니다.')
a = Car()

def test_car_class():
    x = Car()
    print(x.car_name)
    x.set_car_name('Santafe')
    x.get_car_name()
    print(x.car_name)
    x.set_car_drv('4륜')
    x.get_car_name()
    x.set_car_fuel('전기')
    x.get_car_fuel()
    x.set_car_state('브레이크고장')
    x.get_car_state()
    x.set_car_speed(100)
    x.get_car_speed()
    x.stop()
    x.start()
    x.move_forward(100)
    x.move_backward(10)
    return x

x = test_car_class()
type(x)

print('-'*100)


class CarCenter():
    price = {'정상':10, '브레이크고장':1000, '전조등고장':2000, '후미등고장':3000, '연료부족':4000,
             '타이어펑크':5000, '엔진오일부족':6000, '냉각수부족':7000, '폐차처리':9000}

    def __init__(self):
        self.fix_cost = 0
        self.fixed_list = {}
        # self.accent = Car()

    def fix_car(self, auto):
        print("상태 : {}".format(auto.car_state))
        self.fix_cost = CarCenter.price[auto.car_state]
        self.fixed_list[auto.car_name] = auto.car_state
        print('[{0}]{1}[{2}]{3}[{4}]{5}'.format(
            auto.car_name, "의", auto.car_state, " 수리 완료, 비용은 ", self.fix_cost, "원 입니다."))

    def set_car_drv(self, auto, drv):
        auto.car_drv = drv
        auto.set_car_drv(drv)
        # self.accent.car_drv = drv
        print("차의 구동 방식이 [", auto.car_drv, "]으로 변경 되었습니다.")

    def get_car_drv(self, auto):
        return auto.car_drv

    def set_car_fuel(self, auto, fuel):
        auto.car_fuel = fuel
        print("차의 연료 방식이 [", auto.car_fuel,"]로 변경 되었습니다")

    def get_car_fuel(self, auto):
        return auto.car_fuel

    def get_fixed_list(self, auto):
        fixed_item = self.fixed_list[auto.car_name]
        cost = CarCenter.price[fixed_item]
        return '[' + fixed_item + '] : [' + str(cost) + ']원'

benz = CarCenter()
x.set_car_name('CLS')
x.set_car_state('브레이크고장')
print(benz.fix_car(x))







