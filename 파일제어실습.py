# Q.1

class item_info:

    def __init__(self):
        self.info = open('item_info.txt', 'w')
        self.sale = open('item_sale.txt', 'w')
        self.name_list = []
        self.name = 0
        self.price = 0
        self.total = 0
        self.guide = 0
        self.qty = 0
        self.menu = {1:'item_info', 2:'item_sale', 3:'item_total', 0:'종료'}

    def menu(self):

        while True:
            self.guide = int(input('Select Menu:\n 1.품목 정보 등록\n 2.판매 정보 등록\n 3.판매 현황표 출력\n 0.종료'))
            x = self.menu[self.guide]

            if x == 1:
                self.name = input('Input item name:')
                self.price = input('Input item price:')
                self.info.write(self.name)
                self.info.write(self.price)
                for x in self.name:
                    self.name_list.append(x)

            elif x == 2:
                self.name = input('Input item name:')
                x = self.name in self.name_list
                if x == 0:
                    self.name = input('Input item name:')
                    self.price = input('Input item price:')
                    self.qty = input('Input item QTY:')
                    self.info.write(self.name)
                    self.info.write(self.price)
                    self.sale.write(self.name)
                    self.sale.write(self.price)
                    self.sale.write(self.qty)
                else:
                    self.qty = input('Input item QTY:')
                    self.sale.write(self.name)
                    self.sale.write(self.price)
                    self.sale.write(self.qty)
                    self.sale.write(self.price * self.qty)
                print('\n')

            elif x == 3:
                print('{0:^50}'.format('*** Sales Table ***'))
                print()


            else:
                print('종료되었습니다.')
                break


print(3 in [1, 2, 4])

