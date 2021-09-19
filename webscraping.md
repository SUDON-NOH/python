<h1>Web Scraping</h1>

Import modules</h3>
chrome://version 에서 브라우저의 버전을 확인하고, 그에 맞는 chromedriver를 설치해야 한다.
<br></br>

```python
from selenium import webdriver
```
selenium 은 주로 Login , 페이지 이동 등 브라우저를 핸들링하는데 사용  
<br></br>

```python
from bs4 import BeautifulSoup
```
BeautifulSoup 은 웹페이지에 존재하는 태그에 접근해 필요한 내용을 추출
<br></br>

```python
import datetime
```
datetime 은 추후에 브라우저 이동 시간을 조절하기 위해 사용
<br></br>

```python
import time
```
time 은 실행 중 delay 걸리는 부분을 해소하기 위해 사용
<br></br>

```python
import pandas as pd
```
pandas 는 추출한 데이터를 DataFrame 형태로 만드는데 사용


```python


# Headless 모드
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
print(1)
# UserAgent 값을 바꿔서 Headless 탐지를 막는다.
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

print(2)
driver = webdriver.Chrome('chromedriver route')
print(3)
driver.implicitly_wait(5)
print(4)
# login

driver.get('website address')

time.sleep(15)

driver.find_element_by_name('j_id0:j_id6:j_id7:form:j_id53').send_keys('UserID')
driver.find_element_by_name('j_id0:j_id6:j_id7:form:j_id55').send_keys('UserPW')
driver.find_element_by_xpath('//*[@id="j_id0:j_id6:j_id7:form:usr-pwd-auth"]/div[3]/input').click()

print(5)

time.sleep(10)

def doScrollDown(whileSeconds):

    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        time.sleep(1)

        if datetime.datetime.now() > end:
            break


doScrollDown(100)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# '태그', attrs={'태그 속성':'속성 명'}
title = soup.find_all('span', attrs={'class':'body'})
date = soup.find_all('div', attrs={'class':'head'})


list_title = []
list_date = []

for i, r in zip(title, date):

    list_title.append(i.text)
    list_date.append(r.text)

data_table = {'TITLE':list_title, 'DATE':list_date}
data_frame = pd.DataFrame(data_table)
data_frame.to_excel('data_title.xlsx', engine='xlsxwriter')

```
