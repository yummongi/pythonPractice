import imp
import time
import random

print('골라줘 메뉴!')
print('AI 가 추천해주는 메뉴는?')

li = ["김치찌개", "된장찌개", "햄버거", "치밥", "국밥"]
samplelist = random.sample(li,1)

for i in range(5, 0, -1):
     print('메뉴추천중입니다. 남은시간',f'{i}..')
     time.sleep(1)
# print('4..')
# time.sleep(1)
# print('3..')
# time.sleep(1)
# print('2..')
# time.sleep(1)
# print('1..')
# time.sleep(1)
print('분석을 통한 오늘의 추천 메뉴를 추천 드립니다.')
print('오늘의 추천메뉴는',samplelist,'입니다.')