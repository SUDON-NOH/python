class Football:

    def __init__(self):
        print('Class_Football_Game')

    def members(self, list_1):
        member_list = []
        for x in range(0, len(list_1) - 1):
            if x == 0:
                del (list_1[0])
            y = list_1[x]
            member_1 = y.split(',')                   # list의 각 객체들을 1개씩 split해서 리스트로 만든 후
            z = member_1[-1].rstrip('\n')             # csv 줄바꿈 현상에서 나오는 '\n' 글자를 삭제
            del (member_1[-1])
            member_1.append(z)
            member_list.append(member_1)              # 다시 member_list로 묶음
        return member_list

    def extraction_name(self, list_1):                # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        name_list = []                                # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):               # 추출하는 함수
            name_list.append(list_1[x][0])
        return name_list

    def extraction_stats(self, list_1):               # 여기서 list는 위에 members 함수로 뽑아낸 리스트를
        stats_list = []                               # 활용해서 각 리스트 인덱스 0번에 위치한 선수들의 이름을
        for x in range(0, len(list_1)):               # 추출하는 함수
            stats_list.append(list_1[x][3:10])
        return stats_list

    def change_int(self, list_1):                     # Str 문자열을 int 로 뽑는다.
        return [ [ int(y) for y in x ]for x in list_1]
    
    def ability(self, list_1, list_2):                # 선수명과 스텟
        for x in range(0, len(list_1)):               # list_1 에는 선수명 목록
            list_2[x].insert(0, list_1[x])            # list_2 는 능력치 목록
        return list_2
    




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

print(a.ability(name1, stats1))
print(a.ability(name2, stats2))
