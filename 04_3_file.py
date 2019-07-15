# 04_3_파일 읽고 쓰기

# open()/read()/write()/close()


# 파일객체 = open('파일명', '옵션')     # 옵션 = 'w' , 'r' , 'a'
f = open('C:/Users/CPB06GameN/Desktop/file.txt', 'w')           # write, 파일이 없는 경우 생성한다. 있으면 삭제
                # 파일 경로는 \이 아닌 /을 사용

# f = open('file.txt', 'w')           # write, 파일이 없는 경우 생성한다. 있으면 삭제
f.write('1번째 줄입니다.\n')
f.write('2번째 줄입니다.\n')
f.write('3번째 줄입니다.\n')
f.close()


f = open('file.txt', 'r')          # read, 읽기 모드, 쓰기 불가능
# print(type(f))
result = f.read()
print(result)
# close()


f = open('file.txt', 'a')         # append, 파일 추가
                                  # 파일이 있으면 내용을 끝에 추가
f.write('4번째를 <추가> 중 입니다')
f.close()

# =========================================================================================================

f = open('file_line.txt','w')
for k in range(1, 101):
    data = '{:>3} 번째 줄입니다\n'.format(k)
    f.write(data)
f.close()

f = open('file_line.txt','r')
for k in range(1, 101):
    line = f.readline()
    print(line, end = '')         # 앞서 \n 로 줄을 바꿨는데 중복되어 2번 바꾸는 것을 무마시켜주는 기능
f.close()


# 파일을 line 단위로 읽기, 읽기 종료를 자동으로 처리
f = open('file_line.txt','r')
while True:
    line = f.readline()
    if not line : break
    print(line, end = '')
f.close()

f = open('file_line.txt','r')
lines = f.readline()            # 모든 줄을 다 읽고 리스트로 반환
print(lines)
for line in lines:
    print(line, end = '')

# for k in range(len(lines)):           피해야하는 스타일
#     print(lines[k], end = '')
f.close()


# with 문 사용
# with 함수 as 객체:
# with 문 범위내에서만 객체가 유효
# with 문 종료시 객체는 삭제
with open('file_line.txt','r') as f:
    lines = f.readline()
    print(lines)
    for line in lines:
        print(line, end='')


# coffee_sales.txt 실습
# with open('coffee_sales.txt', 'r', encoding='UTF-8') as f:
#     while True:
#         line = f.readline()
#         if not line: break
#         print(line, end = '')

with open('coffee_sales.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line, end='')



with open('coffee_sales.txt', 'r', encoding='UTF-8') as f:
    header = f.readline()
    print(type(header))
    print(header)
    header_list = header.split()  # header를 list 로 추출
    print(header_list)            # ['날짜', '에스프레소', '아메리카노', '카페라테', '카푸치노']
    data_list = []
    date = []
    espresso = []
    americano = []
    cafelatte = []
    cappucino = []
    while True:
        line = f.readline()
        if not line : break
        row = line.split()
        data_list.append(row)
        espresso.append(int(row[1]))
        americano.append(int(row[2]))
        cafelatte.append(int(row[3]))
        cappucino.append(int(row[4]))
        date.append(row[0])
        print('에스프레소', espresso, '판매량:', sum(espresso),
              '평균:', sum(espresso)/len(espresso))
        print('아메리카노', americano, '판매량:', sum(americano),
              '평균:', sum(americano)/len(americano))
        print('카페라뗴 ', cafelatte, '판매량:', sum(cafelatte),
              '평균:', sum(cafelatte)/len(cafelatte))
        print('카푸치노', cappucino, '판매량:', sum(cappucino),
              '평균:', sum(cappucino)/len(cappucino))
        print(data_list)

# 예외 처리
try:
    with open('hello.txt', 'r') as f:
        while True:
            data = f.readline()
            if not data:
                break
except FileNotFoundError:
    print("파일이 없어요")

print('정상 처리 종료')