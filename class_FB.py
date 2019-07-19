class Prepare_F:

    def __init__(self):
        print('Class_Prepare_F')

    def members(self, list_1):
        self.member_list = []
        for x in range(0, len(list_1) - 1):
            if x == 0:
                del (list_1[0])
            y = list_1[x]
            member_1 = y.split(',')                         # list의 각 객체들을 1개씩 split해서 리스트로 만든 후
            z = member_1[-1].rstrip('\n')                   # csv 줄바꿈 현상에서 나오는 '\n' 글자를 삭제
            del (member_1[-1])
            member_1.append(z)
            self.member_list.append(member_1)               # 다시 member_list로 묶음
        return self.member_list

    def members2(self, list_1):
        self.member_list = []
        for x in range(0, len(list_1) - 1):
            y = list_1[x]
            self.member_1 = y.split(',')                    # list의 각 객체들을 1개씩 split해서 리스트로 만든 후
            z = self.member_1[-1].rstrip('\n')              # csv 줄바꿈 현상에서 나오는 '\n' 글자를 삭제
            del (self.member_1[-1])
            self.member_1.append(z)
            self.member_list.append(self.member_1)          # 다시 member_list로 묶음

        return self.member_list

    def extraction_name(self, list_1):                      # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        self.name_list = []                                 # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):                     # 추출하는 함수
            self.name_list.append(list_1[x][0])
        return self.name_list


    def extraction_name2(self, list_1):                      # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        self.name_list = []                                 # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):                     # 추출하는 함수
            self.name_list.append(list_1[x][0:2])
        return self.name_list


    def extraction_npo(self, list_1):
        self.npo_list = []
        a = []
        for x in range(0, len(list_1)):
            a = list_1[x][0] + ' ' + list_1[x][1] + ' ' + list_1[x][2] + ' ' + list_1[x][9]
            self.npo_list.append(a)
        return self.npo_list

    def extraction_stats(self, list_1):                      # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        self.stats_list = []                                 # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):                      # 추출하는 함수
            self.stats_list.append(list_1[x][3:10])
        return self.stats_list

    def change_int(self, list_1):                            # Str 문자열을 int 로 뽑는다.
        return [[int(y) for y in x] for x in list_1]

    def ability(self, list_1, list_2):                       # 선수명과 스텟
        for x in range(0, len(list_1)):                      # list_1 에는 선수명 목록
            list_2[x].insert(0, list_1[x])                   # list_2 는 능력치 목록
        return list_2

    def field_ability(self, list_3):                    # list_3 은 ability에서 선수명과 능력치를 합한 것
        self.speed = {}                                 # self.speed 등으로 불러와서 사용 가능
        self.shot = {}                                  # dict 형태로 구현
        self.pass_n = {}
        self.dribbling = {}
        self.defence = {}
        self.physical = {}
        self.ovr = {}
        for x in range(0, len(list_3)):
            a = {list_3[x][0] : list_3[x][1]}
            self.speed.update(a)
        for x in range(0, len(list_3)):
            b = {list_3[x][0] : list_3[x][2]}
            self.shot.update(b)
        for x in range(0, len(list_3)):
            c = {list_3[x][0] : list_3[x][3]}
            self.pass_n.update(c)
        for x in range(0, len(list_3)):
            d = {list_3[x][0] : list_3[x][4]}
            self.dribbling.update(d)
        for x in range(0, len(list_3)):
            e = {list_3[x][0] : list_3[x][5]}
            self.defence.update(e)
        for x in range(0, len(list_3)):
            f = {list_3[x][0] : list_3[x][6]}
            self.physical.update(f)
        for x in range(0, len(list_3)):
            g = {list_3[x][0] : list_3[x][7]}
            self.ovr.update(g)
        return self.speed, self.shot, self.pass_n, self.dribbling, self.defence, self.physical, self.ovr

    def gk_ability(self, list_3):                    # list_3 은 ability에서 선수명과 능력치를 합한 것
        self.diving = {}                             # self.speed 등으로 불러와서 사용 가능
        self.handling = {}                           # dict 형태로 구현
        self.kick = {}                               # 골키퍼 플레이어용 능력치 추출기
        self.reaction = {}
        self.speed_gk = {}
        self.site_selection = {}
        self.ovr_gk = {}
        for x in range(0, len(list_3)):
            a = {list_3[x][0] : list_3[x][1]}
            self.diving.update(a)
        for x in range(0, len(list_3)):
            b = {list_3[x][0] : list_3[x][2]}
            self.handling.update(b)
        for x in range(0, len(list_3)):
            c = {list_3[x][0] : list_3[x][3]}
            self.kick.update(c)
        for x in range(0, len(list_3)):
            d = {list_3[x][0] : list_3[x][4]}
            self.reaction.update(d)
        for x in range(0, len(list_3)):
            e = {list_3[x][0] : list_3[x][5]}
            self.speed_gk.update(e)
        for x in range(0, len(list_3)):
            f = {list_3[x][0] : list_3[x][6]}
            self.site_selection.update(f)
        for x in range(0, len(list_3)):
            g = {list_3[x][0] : list_3[x][7]}
            self.ovr_gk.update(g)
        return self.diving, self.handling, self.kick, self.reaction, self.speed_gk, self.site_selection, self.ovr_gk

    # 선수 번호 매김
    def numbering_fd(self, list_1):                 # list_1 은 def field_ability(self, list_3): 함수에서 나온 값이다.
        # 선수 번호                                   # self.ovr
        player_num = {}
        for i, name in enumerate(list_1):
            player_num[i] = name
        return player_num
        # {0: 'L.Messi', 1: 'H.KANE', 2: 'A.Lacazette'.....

    def numbering_gk(self, list_1):                 # list_1은 def gk_ability(self, list_3): 함수에서 나온 값이다.
        # 키퍼 번호
        gk_num = {}
        for i, name2 in enumerate(list_1):
            gk_num[i] = name2
        return gk_num
        # {0: 'De Gea', 1: 'Hugo Lloris', 2: 'J.Oblak', 3: 'M. ter Stegen', 4: 'W.Szczesny'}




class Play_1:
    def __init__(self):
        self.a = 0

    def rps_p(self):
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('=' * 140)
        print('{0:>70}'.format('Soccer Game ! !'))
        print('{0:>70}'.format('<가위바위보로 선수 선택의 선 후를 가립니다.>'))

        player_1 = input('플레이어1 의 이름을 입력하세요 : ')
        player_2 = input('플레이어2 의 이름을 입력하세요 : ')

        players = [player_1, player_2]

        selection_1 = int(input('''
        # %s 님! 다음 중 무엇을 낼것인지 고르세요 

        1. 가위
        2. 바위
        3. 보

        ''' % player_1))

        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')

        selection_2 = int(input('''
        # %s 님! 다음 중 무엇을 낼것인지 고르세요 

        1. 가위
        2. 바위
        3. 보

        ''' % player_2))
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')

        if selection_1 == 1:
            selection_1 = '가위'
        elif selection_1 == 2:
            selection_1 = '바위'
        elif selection_1 == 3:
            selection_1 = '보'
        else:
            selection_1 = '잘못된 입력 '

        if selection_2 == 1:
            selection_2 = '가위'
        elif selection_2 == 2:
            selection_2 = '바위'
        elif selection_2 == 3:
            selection_2 = '보'
        else:
            selection_2 = '잘못된 입력 '

        print("\n {0} 님이 {1}를 내셨습니다.".format(player_1, selection_1))
        print("\n {0} 님이 {1}를 내셨습니다.".format(player_2, selection_2))

        if selection_2 == selection_1:
            print('\n', "둘 다 {0}로 비겼습니다.".format(selection_2))
        elif selection_2 == "가위":
            if selection_1 == "바위":
                self.a = player_1
                print('\n', "{0} 님이 {1}로 승리하였습니다!".format(player_1, selection_1))
            elif selection_1 == "보":
                self.a = player_2
                print('\n', "{0} 님이 {1}로 승리하였습니다!".format(player_2, selection_2))
        elif selection_2 == "바위":
            if selection_1 == "보":
                self.a = player_1
                print('\n', "{0} 님이 {1}로 승리하였습니다!".format(player_1, selection_1))
            elif selection_1 == "가위":
                self.a = player_2
                print('\n', "{0} 님이 {1}로 승리하였습니다!".format(player_2, selection_2))
        elif selection_2 == "보":
            if selection_1 == "가위":
                self.a = player_1
                print('\n', "{0} 님이 {1}로 승리하였습니다!".format(player_1, selection_1))
            elif selection_1 == "바위":
                self.a = player_2
                print('\n', "{0} 님이 {1}로 승리하였습니다!".format(player_2, selection_2))
        else:
            print('\n', "잘못된 입력입니다.")

        return self.a

class Prepare_M:

    def __init__(self):

        print('Class_Prepare_M')
        self.member_0 = open('C:/Users/CPB06GameN/PycharmProjects/Python/member.csv', 'r', encoding='UTF-8')
        self.field_member = self.member_0.readlines()
        # # 원본 데이터 - 필드 플레이어용
        print('원본 데이터', '\n', self.field_member)



        self.member_1 = open('C:/Users/CPB06GameN/PycharmProjects/Python/member2.csv', 'r', encoding='UTF-8')
        self.GK_member = self.member_1.readlines()
        # # 원본 데이터 - 골키퍼 플레이어용
        print('원본 데이터', '\n', self.GK_member)

        self.C = Play_1
        self.j_1 = Prepare_F()
        j_2 = self.j_1.members(self.field_member)
        j_3 = self.j_1.members(self.GK_member)

        self.j_5 = self.j_1.members2(self.field_member)     # # jamjam 함수용  플레이어
        self.j_6 = self.j_1.members2(self.GK_member)        # # jamjam 함수용  골키퍼

        # # 선수 이름 추출
        self.name1 = self.j_1.extraction_name(j_2)
        print('필드 플레이어 선수 이름', '\n', self.name1)
        self.name2 = self.j_1.extraction_name(j_3)
        print('골키퍼 플레이어 선수 이름', '\n', self.name2)
        self.npo1 = self.j_1.extraction_npo(j_2)
        print('필드 플레이어 이름, 포지션, OVR', '\n', self.npo1)
        self.npo2 = self.j_1.extraction_npo(j_3)
        print('필드 플레이어 이름, 포지션, OVR', '\n', self.npo2)

        self.tt = self.j_1.numbering_fd(self.name1)
        self.jamname = self.j_1.extraction_name2(j_2)
        self.jamname2 = self.j_1.numbering_fd(self.jamname)

        # # 선수 능력치 추출
        self.ext1 = self.j_1.extraction_stats(j_2)
        print('필드 플레이어 능력치 추출', '\n', self.ext1)
        self.ext2 = self.j_1.extraction_stats(j_3)
        print('골키퍼 플레이어 능력치 추출', '\n', self.ext2)

        # # 선수 능력치 int형으로 변환
        self.stats1 = self.j_1.change_int(self.ext1)
        print('필드 플레이어 능력치 추출(int형)', '\n', self.stats1)
        self.stats2 = self.j_1.change_int(self.ext2)
        print('골키퍼 플레이어 능력치 추출(int형)', '\n', self.stats2)

        # # 이름 + 능력치
        self.ability1 = self.j_1.ability(self.name1, self.stats1)
        self.ability2 = self.j_1.ability(self.name2, self.stats2)
        print('필드 플레이어 이름 + 능력치', '\n', self.ability1)
        print('골키퍼 플레이어 이름 + 능력치', '\n', self.ability2)


        # # 각 플레이어별 능력치
        self.field_j_1 = self.j_1.field_ability(self.ability1)
        self.gk_j_1 = self.j_1.gk_ability(self.ability2)

        print('필드 플레이어 스피드', '\n', self.j_1.speed)
        print('필드 플레이어 드리블', '\n', self.j_1.dribbling)
        print('필드 플레이어 슛팅', '\n', self.j_1.shot)
        print('메시의 스피드', '\n', self.j_1.speed['L.Messi'])
        print(self.j_1.pass_n)
        print(self.j_1.dribbling)
        print(self.j_1.defence)
        print(self.j_1.physical)
        print(self.j_1.ovr)


        self.ff_n = self.j_1.numbering_fd(self.j_1.ovr)
        self.gk_n = self.j_1.numbering_gk(self.j_1.ovr_gk)

        self.xx_n = self.j_1.numbering_fd(self.npo1)            # 재광이 함수 반환
        self.xy_n = self.j_1.numbering_gk(self.npo2)            # 재광이 함수 반환

    def message(self):
        for i in range(len(self.npo1)):  # name 1 = a.extraction_npo(x) # x : a.members(field_member)
            # ['L.Messi CF FC BARCELONA 87', 'H.KANE CF TOTTENHAM 79', 'A.L..., , ,  ]
            print('Field Players')
            print('{0:<3}. {1}'.format(i, self.xx_n[i]))  # 필드 선수 리스트 출력하기위한 함수
            print('\n')
            print('\n')
            print('\n')
        for j in range(len(self.npo2)):
            print('GK Players')
            print('{0:<3}. {1}'.format(j, self.xy_n[j]))  # 골키퍼 선수 리스트 출력하기위한 함수

    def fd_ab(self):                    # 필드 플레이어 능력치 검색 함수
        print('필드 플레이어 정보를 확인 한 후 진행합니다.')

        # print("Field Player\n번호  이름/포지션/소속/OVR")
        # # 재민이 선수 목록

        while True:
            self.fd_a_number = input(
                'A: SPEED\nB: SHOT\nC: PASS\nD: Dribbling\nE: Defence\nF: Physical\nG: Ovr\nZ: END')
            self.dic_FD = {'A': self.j_1.speed, 'B': self.j_1.shot,
                           'C': self.j_1.pass_n, 'D': self.j_1.dribbling,
                           'E': self.j_1.defence, 'F': self.j_1.physical,
                           'G': self.j_1.ovr}
            self.aa = []
            player_z = 0

            AAA = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

            self.ppp = {'A': 'SPEED', 'B': 'SHOT','C': 'PASS','D': 'Dribbling','E': 'Defence','F': 'Physical','G': 'Ovr','Z': 'END'}

            # while True:
            if self.fd_a_number in AAA:
                x = self.dic_FD[self.fd_a_number]
                print(self.ppp[self.fd_a_number])
                print(x)
                z = input('확인 후 ENTER를 입력하세요.')

                # while True:
                #     print('선수들의', self.ppp[self.fd_a_number], '를 확인합니다.')
                #     player_z = int(input(
                #         """
                #            선수들의 번호를 입력하세요.\n
                #            전체보기는 "999"를 입력하세요.\n
                #            멈추려면 "END"를 입력하세요.
                #         """))
                #     if player_z != 'END':
                #         yy = self.ff_n[player_z]
                #         y = x[yy]
                #         self.aa.append(y)
                #         print(y)
                #         print(self.aa)
                #
                #     elif player_z == '999':
                #         print(x)
                #
                #     else:
                #         break

            else:
                print('종료되었습니다.')
                break


    def gk_ab(self):
        print('골키퍼 정보를 확인 한 후 진행합니다.')
        while True:
            self.GK_a_number = input('A: Diving\nB: Handling\nC: Kick\nD: Reaction\nE: Speed\nF: Site-Selection\nG: Ovr\nZ: END')
            x = {}
            # print("GK Player\n번호  이름/포지션/소속/OVR")
            # 재민이 선수 목록

            self.dic_GK = {'A': self.j_1.diving, 'B': self.j_1.handling, 'C': self.j_1.kick, 'D': self.j_1.reaction,
                      'E': self.j_1.speed, 'F': self.j_1.site_selection, 'G': self.j_1.ovr_gk}

            aa = []
            player_z = 0
            AAA = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            self.ppp = {'A': 'Diving', 'B': 'Handling', 'C': 'Kick', 'D': 'Reaction', 'E': 'Speed', 'F': 'Site-Selection',
                        'G': 'Ovr', 'Z': 'END'}

            # while True:
            if self.GK_a_number in AAA:
                x = self.dic_GK[self.GK_a_number]
                print(self.ppp[self.GK_a_number])
                print(x)
                z = input('확인 후 ENTER를 입력하세요.')
                # while True:
                #             #     player_z = int(input('선수들의 번호를 입력하세요.'))
                #             #     if player_z != 'END':
                #             #         yy = self.ff_n[player_z]
                #             #         y = x[yy]
                #             #         aa.append(y)
                #             #         print(y)
                #             #         print(x)
                #             #     else:
                #             #         break
            else:
                print('종료되었습니다.')
                break





if __name__ == '__main__':
    a = Prepare_M()
    print(a.j_1.speed['L.Messi'])
    print(a.j_1.ovr)
    print(a.ff_n)

# class players_ab:
#
#     def __init__(self):
#         j_4 = Prepare_M()
#


class jamjam:

    def __init__(self):
        self.jam = Prepare_M()

    def select_player(self, lists, select,player_dic):
        # list : 선수 1명의 능력치 list  : ['son',10,20,40,80,20,50,90] # 90자리 ,ovr    [7]
        # cf = [] # 공격수 :[['son',10,20,40,80,20,50],['jam',10,20,40,80,20,50],['yum',10,20,40,80,20,50]]
        # cm = [] # 미드필더 : 형식 동일
        # cb = [] # 수비 : 형식 동일
        # wb = [] # 수비 : 형식 동일
        # gk = [] # 골키퍼
        print('HEAR::!!!!!!!!!!!!!!!!!!', lists)
        print(select)
        if lists[1] == 'CF':  # 공격수였음
            if select == lists[1]:
                player_dic['CF'].append(lists)
            elif select == 'CM':  # CM선택
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.3)
                player_dic['CM'].append(lists)
            elif select == 'CB':  # CB면
                # print('finish')
                # lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                # lists[-1] = int(lists[-1]) -(int(lists[-1])*0.5)

                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['CB'].append(lists)

            elif select == 'WB':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['WB'].append(lists)
            elif select == 'GK':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['GK'].append(lists)
            else:
                print('error1')
                pass

        elif lists[1] == 'CM':  # 공격수였음
            if select == lists[1]:
                player_dic['CM'].append(lists)
            elif select == 'CF':  # CM선택
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.3)
                player_dic['CF'].append(lists)
            elif select == 'CB':  # CB면
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['CB'].append(lists)
            elif select == 'WB':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['WB'].append(lists)
            elif select == 'GK':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['GK'].append(lists)
            else:
                print('error2')
                pass

        elif lists[1] == 'CB':  # 공격수였음
            if select == lists[1]:
                player_dic['CB'].append(lists)
            elif select == 'CM':  # CM선택
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.3)
                player_dic['CM'].append(lists)
            elif select == 'CF':  # CB면
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['CF'].append(lists)
            elif select == 'WB':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['WB'].append(lists)
            elif select == 'GK':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['GK'].append(lists)
            else:
                print('error3')
                pass

        elif lists[1] == 'WB':  # 공격수였음
            if select == lists[1]:
                player_dic['WB'].append(lists)
            elif select == 'CM':  # CM선택
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.3)
                player_dic['CM'].append(lists)
            elif select == 'CB':  # CB면
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['CB'].append(lists)
            elif select == 'CF':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.5)
                player_dic['CF'].append(lists)
            elif select == 'GK':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['GK'].append(lists)
            else:
                print('error')
                pass
        elif lists[1] == 'GK':  # 공격수였음
            if select == lists[1]:
                player_dic['GK'].append(lists)
            elif select == 'CM':  # CM선택
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['CM'].append(lists)
            elif select == 'CB':  # CB면
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['CB'].append(lists)
            elif select == 'WB':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['CF'].append(lists)
            elif select == 'CF':
                lists[-1] = int(lists[-1]) - (int(lists[-1]) * 0.9)
                player_dic['CF'].append(lists)
            else:
                print('error')
                pass


        else:
            print('error')

        return player_dic



    def jimmy_print_position(self):
            for i in self.player_dic['CF']:
                print('{0:=^20}'.format(i[0]), end='')
            print()

            # print('{0:=^120}'.format('0'))

            for o in self.player_dic['CM']:
                print('{0:=^20}'.format(o[0]), end='')
            print()


            for wb in range(len(self.player_dic['WB'])):
                if wb == 0:
                    print('{0:=^15}'.format(self.player_dic['WB'][wb][0]), end='')
                    for cb in self.player_dic['CB']:
                        print('{0:=^15}'.format(cb[0]), end='')
                else:
                    print('{0:=^15}'.format(self.player_dic['WB'][wb][0]), end='')
            print()

            for p in self.player_dic['GK']:
                print('{0:=^60}'.format(p[0]))


    def jamjam2(self):
        player_num = self.jam.jamname2
        # print('player_num', player_num)
        player =self.jam.j_5     # field_member
        # print(player)
        player_name = self.jam.j_1.extraction_name2(player)  # name
        # print('player_name',player_name)
        player_stats = self.jam.j_1.extraction_stats(player)
        # print('player_stats',player_stats)
        # print('here!!!!!!!',self.jam.change_int(player_stats))
        player_non_str = self.jam.j_1.ability(player_name, self.jam.j_1.change_int(player_stats))
        # print('self.jam.j_1.change_int(player_stats)',self.jam.j_1.change_int(player_stats))
        # print('player_non_str',player_non_str)

        self.player_dic = {}
        posit_list = ['CF', 'CM', 'CB', 'WB', 'GK']
        for posit in posit_list:  # 포지션마다 딕셔너리 선언
            self.player_dic[posit] = []

        while True:
            # message()
            player = int(input('선수이름을 고르시오 >> \n'
                               '종료하시려면 "-1"을 입력하세요'))
            if player == -1:
                break

            # print(player_num[player])
            # kipper = int(input('키퍼 이름을 고르시오 >> '))
            # print(player)
            position = input('포지션을 선택하세요')
            # print(player_non_str)
            # result = []
            # result.append(player_non_str)
            # print(result)
            # print('HERE>>>>>>>>>>',player_non_str)
            print(position)
            for name in player_non_str:
                # print('player_num[player][0]:',player_num[player][0])
                # print('name',print(),name[0])
                # print('player_num',player_num[player][0])
                if name[0][0] == player_num[player][0]:
                    # print('0')
                    # print('HERE!!!!!!!!!!!!!!!!!!!!!!!',name, position, self.player_dic)
                    self.player_dic = self.select_player(name[0], position, self.player_dic)
                    # print('1')
                    # print(self.player_dic)
                    self.jimmy_print_position()
                    # asd = input('x')
                else:
                    # print('pass')
                    pass

