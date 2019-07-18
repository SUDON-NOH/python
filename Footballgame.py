class Football:

    def __init__(self):
        print('Class_Football_Game')

    def members(self, list):
        member_list = []
        for x in range(0, len(list) - 1):
            if x == 0:
                del (list[0])
            y = list[x]
            member_1 = y.split(',')
            z = member_1[-1].rstrip('\n')
            del (member_1[-1])
            member_1.append(z)
            member_list.append(member_1)
        return member_list

    def extraction_name(self, list):
        name_list = []
        for x in range(0, len(list)):
            name_list.append(list[x][0])
        return name_list

    def extraction_stats(self, list):
        stats_list = []
        for x in range(0, len(list)):
            stats_list.append(list[x][3:10])
        return stats_list




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
print(a.extraction_name(y))
print(len(x))
print(len(y))
print(a.extraction_stats(x))
print(a.extraction_stats(y))

