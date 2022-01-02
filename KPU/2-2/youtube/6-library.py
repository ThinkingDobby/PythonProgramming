# 외장 함수
# import 해서 사용

import sys
print(sys.argv) # 파일 열 때 인자

import pickle   # 딕셔너리 저장

import time
print(time.time())
for i in range(0, 5):
    print(i)
    time.sleep(1)

import webbrowser
# webbrowser.open("http://rabbito.kr")
