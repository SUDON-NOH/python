from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

"""
====================================================================================
38 커뮤니케이션 홈페이지에서 종목코드 정보 불러오기
====================================================================================
"""


# 키워드를 친 상태의 url을 입력
address = 'http://www.38.co.kr/html/forum/?keyword=%B9%D9%C0%CC%BF%C0'
# 웹페이지 하단에 나온 페이지의 수를 입력
num = str(8)
# 저장할 폴더 경로 설정
file_load = 'C:/Users/SD NOH/Desktop/노수돈'
# 파일 이름 설정
file_name = '회사정리'


code_list = []

for i in range(int(num)):

    i = i+1
    address = address+'&page='+str(i)
    html = urlopen(address)
    bs0bj = BeautifulSoup(html.read(), "html.parser")

    list = bs0bj.findAll("tr",{"onmouseout":"this.style.background='#FFFFFF'"})


    for x in list:

        code_list.append(x.get_text(strip=True)[0:6])










"""
===================================================================================
web page의 html을 불러와서 정보 수집
===================================================================================
"""

dataframe = pd.DataFrame()

for code_num in code_list:

    # url에 해당하는 html 정보 불러오기
    url = 'http://www.38.co.kr/html/forum/board/?code='+code_num+'&o=cinfo'
    # url = 'http://www.38.co.kr/html/forum/board/?code=286530&o=cinfo'
    html = urlopen(url)
    bs0bj = BeautifulSoup(html.read(), "html.parser")

    # 회사 개요에 대한 내용을 입력하기 위해 사용
    info_list = []
    # 회사 사업내용에 대한 내용을 입력하기 위해 사용
    contents_list = []
    # 회사 개요 컬럼
    column = []
    # 회사 개요 내용
    content = []
    # 회사 사업 내용
    business_content = ''

    # <table> 태그에 "summary"가 "개요일반"인 것들을 찾음
    list = bs0bj.findAll("table",{"summary":"개요일반"})
    # <table> 태그에 "summary"가 "사업내용"인 것들을 찾음
    list2 = bs0bj.findAll("table",{"summary":"사업내용"})

    for element in list:

        # 한 줄의 text 형식으로 되어있는 요소들을 분리시키기 위해 사용
        info_list.append(element.get_text().splitlines())


    for element2 in list2:

        contents_list.append(element2.get_text().splitlines())

        for i in contents_list[0]:
            if i == "":
                pass
            else:
                # 문자열 내에 있는 /xa0 을 공백으로 바꾸고, /t/t 를 제거하기위해 strip을 사용
                business_content = i.replace(u'\xa0',u'').strip()


    count = 1


    if not info_list:
        pass
        print(code_num)
    else:
        for i in info_list[0]:

            # 공백으로 들어간 부분을 제거하기 위해 사용
            if i == "":
                pass
            elif count%2 == 1:
                # "\xa0" 를 제거하기 위해 strip 사용
                p = i.strip()
                column.append(p)
                count += 1

            else:
                # "\xa0" 를 제거하기 위해 strip 사용
                p = i.strip()
                content.append(p)
                count += 1


        column.append("사업내용")
        content.append(business_content)


        table = dict(zip(column, content))

        df = pd.DataFrame(table, index=[0])
        print(table)

        dataframe = dataframe.append(df)


dataframe.to_excel(file_load+'/'+file_name+'.xlsx')



