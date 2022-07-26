from tkinter import *
import random

#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자
li = ["김치찌개", "된장찌개", "햄버거", "치밥", "국밥"]
samplelist = random.sample(li,1)
# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
label = Label(tk,text='AI 가 추천해주는 메뉴는?') 
# 3. 레이블 배치 실행
#label.pack()
label.pack()
# 예제2) 버튼만들기
#tk = Tk()
# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
def event():
    samplelist = random.sample(li,1)
    button['text'] = samplelist,'추천!'

button = Button(tk,text='추천메뉴',command=event)
#button2 = Button(tk,text='버튼2 입니다.')
button.pack(side=TOP,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
#button2.pack(side=LEFT, padx=10, pady= 10)
# 4. 메인루프 실행
tk.mainloop()

