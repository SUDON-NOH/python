https://rednooby.tistory.com/100 - 


===============================================================================

출력 결과를 Text 파일로 저장

import sys sys.stdout = open('output.txt','w')

print('hello !!!') 이렇게 하면, 화면에 "hello !!!" 가 출력이 되는것이 아니고, output.txt 파일이 생성되고, 그 안에 출력문이 기록됩니다.

이어쓰기 (w 대신에 a를 입력)

open('output.txt','w')

경로 설정하기

open('folder/output.txt','w') 하위폴더를 지정할려면, 폴더 이름을 같이 써주시고, 다른 경로에 있으면, /(루트) 이하의 전체경로를 써주셔야 합니다.

===============================================================================

numpy # 다차원을 1차원으로 변경

a.ravel()

=======================================================================================

파이참 설치시

Consider using the `--user` option or check the permissions.

에러

pip install --user --upgrade setuptools

or

pip install --user setuptools

