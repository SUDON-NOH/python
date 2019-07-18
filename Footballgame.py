class Football:

    def __init__(self):
        print('Class_Football_Game')

    def members(self, list_1):
        self.member_list = []
        for x in range(0, len(list_1) - 1):
            if x == 0:
                del (list_1[0])
            y = list_1[x]
            self.member_1 = y.split(',')                   # list의 각 객체들을 1개씩 split해서 리스트로 만든 후
            z = self.member_1[-1].rstrip('\n')             # csv 줄바꿈 현상에서 나오는 '\n' 글자를 삭제
            del (self.member_1[-1])
            self.member_1.append(z)
            self.member_list.append(self.member_1)              # 다시 member_list로 묶음
        return self.member_list

    def extraction_name(self, list_1):                # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        self.name_list = []                                # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):               # 추출하는 함수
            self.name_list.append(list_1[x][0])
        return self.name_list

    def extraction_stats(self, list_1):               # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        self.stats_list = []                               # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):               # 추출하는 함수
            self.stats_list.append(list_1[x][3:10])
        return self.stats_list

    def change_int(self, list_1):                     # Str 문자열을 int 로 뽑는다.
        return [ [ int(y) for y in x ]for x in list_1]

    def ability(self, list_1, list_2):                # 선수명과 스텟
        for x in range(0, len(list_1)):               # list_1 에는 선수명 목록
            list_2[x].insert(0, list_1[x])            # list_2 는 능력치 목록
        return list_2

    def field_ability(self, list_3):                    # list_3 은 ability에서 선수명과 능력치를 합한 것
        self.speed = {}                                 # self.speed 등으로 불러와서 사용 가능
        self.shot = {}                                  # dict 형태로 구현
        self.pass_n = {}                                # 필드 플레이어용 능력치 추출기
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










member_0 = open('C:/Users/CPB06GameN/PycharmProjects/Python/member.csv', 'r', encoding='UTF-8')
field_member = member_0.readlines()
print(field_member)

member_1 = open('C:/Users/CPB06GameN/PycharmProjects/Python/member2.csv', 'r', encoding='UTF-8')
GK_member = member_1.readlines()
print(GK_member)


a = Football()
x = a.members(field_member)
y = a.members(GK_member)

print(a.extraction_name(x))
name1 = a.extraction_name(x)
print(name1)
print(a.extraction_name(y))
name2 = a.extraction_name(y)
print(len(x))
print(len(y))
print(a.extraction_stats(x))
print(a.extraction_stats(y))
print(a.change_int(a.extraction_stats(x)))
stats1 = a.change_int(a.extraction_stats(x))
print(a.change_int(a.extraction_stats(y)))
stats2 = a.change_int(a.extraction_stats(y))

ability1 = a.ability(name1, stats1)
ability2 = a.ability(name2, stats2)
print(ability1)
print(ability2)

field_a = a.field_ability(ability1)

print(a.speed)
print(a.dribbling)
print(a.shot)


