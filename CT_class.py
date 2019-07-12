# # 클래스 활용 기본 실습 문제
#   1 (1)

class Calculator():

    def __init__(self):
        print('Calculator 생성자 호출')
        self.operator = {1:'+', 2:'-', 3:'*', 4:'/'}
        self.a = 0
        self.b = 0
        self.op = 0

    def calculate(self, a, b, op):
        self.op = self.operator[op]
        return eval('a' + self.op + 'b')


if __name__ == '__main__':
    sec = Calculator()
    print(sec.calculate(10, 5, 2))
    
