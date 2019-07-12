# # 클래스 활용 기본 실습 문제
#   1 (3)

import CCT_class as CCT

class ViewCalculator():

    def __init__(self):
        self.vcal = CCT.ControlCalculator()
        self.sel = ['end', 'pass']

    def DisplayCalculator(self):
        while self.sel != 'end':
            self.sel = input('종료: end // 실행 : pass')
            if self.sel != 'end':
                a = int(input('Number_1'))
                op = int(input("'1:'+', 2:'-', 3:'*', 4:'/'"))
                b = int(input('Number_2'))
                print(a, self.vcal.cal.operator[op], b, '=', self.vcal.cal.calculate(a, b, op))
            else:
                print('종료되었습니다.')

forth = ViewCalculator()
forth.DisplayCalculator()
