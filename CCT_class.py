# # 클래스 활용 기본 실습 문제
#   1 (2)

import CT_class as CT

class ControlCalculator():

    def __init__(self):
        print('ControlCalculator 생성자 호출')
        self.cal = CT.Calculator()

    def calculate(self, a, b, op):
        return self.cal.calculate(a, b, op)



if __name__ == '__main__':
    tir = ControlCalculator()
    print(tir.cal.calculate(10, 8, 1))






