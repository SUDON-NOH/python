# 함수 과제

print('{0:-^70}'.format('Q1'))

def ponderal(kg, cm):
    Standard_weig = (cm - 100) * 0.85
    ponderal_per = kg / Standard_weig * 100
    if ponderal_per <= 90 :
        print('{0:5.2F}%{1}{2}'.format(ponderal_per, ' ', '저체중'))
    elif ponderal_per <= 110 :
        print('{0:5.2F}%{1}{2}'.format(ponderal_per, ' ', '정상'))
    elif ponderal_per <= 120:
        print('{0:5.2F}%{1}{2}'.format(ponderal_per, ' ', '과체중'))
    else:
        print('{0:5.2F}%{1}{2}'.format(ponderal_per, ' ', '비만'))

ponderal(70, 176)

print('{0:-^70}'.format('Q2'))
# 1
def leap_year(year):
    if year % 400 == 0:
        print(year, '은 윤년이다.')
    elif year % 4 == 0 and year % 100 != 0:
        print(year, '은 윤년이다.')
    else:
        print(year, '은 윤년이 아니다.')

leap_year(1994)
leap_year(2000)

# 2
def how_old(birth):
    print(2019 - birth + 1, '세')

# 3
def jisin_12(year):
    x = ["쥐","소","호랑이","토끼","용","뱀","말","양","원숭이","닭","개","돼지"]
    y = (year - 4) % 12
    z = x[y]
    print(year, '은', z, '띠 입니다.')
jisin_12(2019)
jisin_12(2018)
jisin_12(2017)
jisin_12(2016)
jisin_12(2015)
jisin_12(2014)
jisin_12(2013)
jisin_12(2012)
jisin_12(2011)
jisin_12(2010)
jisin_12(2009)
jisin_12(2008)
jisin_12(2007)
jisin_12(2006)
jisin_12(1)
jisin_12(2)
jisin_12(3)
jisin_12(4)
jisin_12(5)
jisin_12(6)

print('{0:-^70}'.format('Q3'))
def grade(point):
    d = {100 >= point and 90 <= point : 'A',
         89 >= point and 80 <= point : 'B',
         79 >= point and 70 <= point : 'C',
         69 >= point and 60 <= point : 'D',
         60 >= point : 'F'}

print('{0:-^70}'.format('Q4'))
def mTOmile(meter):
    mile = meter / 1.609
    print(meter,'m 는', mile, 'mile')
mTOmile(1.609)

print('{0:-^70}'.format('Q5'))
def fToc(fahrenheit):
    celsius = ( fahrenheit - 32) / 1.8
    print('{0}{1}{2}{3:4.2F}{4}'.format('화씨', fahrenheit, '도는 섭씨로', celsius, '도 입니다.'))
fToc(80)

print('{0:-^70}'.format('Q6'))

def yaksoo(number):
    a = []
    for k in range(1, number + 1):
        if number % k == 0:
            a.append(k)
        else:
            pass
    return a
print(yaksoo(2500021))

print('{0:-^70}'.format('Q7'))

def value(a , b):
    if a < 0 & b > 0:
        c = b - a
    elif b < 0 & a > 0:
        c = a - b
    elif a > 0 & b >0:
        if a > b:
            c = a - b
        else:
            c = -(a-b)
    elif a == b:
        c = a - b
    else:
        if a > b:
            c = a - b
        else:
            c = b - a
    return c

print(value(-1, -4))
print(value(10, -5))
print(value(-10, -9))
print(value(10, 10))
print(value(-10, -10))

print('{0:-^70}'.format('Q8'))

