import tkinter as tk
import random
import time
import pandas as pd
window = tk.Tk()
window.title('타자연습')
window.geometry('500x300+100+100')
tk.Label()

data = pd.read_csv('data.CSV', encoding='cp949')
Wl = data['문장']



CHO = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 
    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
JUNG = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 
    'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]
JONG = [
    '', 'ㄱ','ㄲ','ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 
    'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 
    'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

idx = 0
random.shuffle(Wl)


def func2():  #시작 변수
     global start_time
     global dlqtl
     start_time = time.time()
     prs.config(text=Wl[0])
     dlqtl = time.time()
     
    
def func3():  #종료 변수
     global start_time
     global end_time
     global duration
     end_time = time.time()
     duration = round(end_time - start_time, 2)
     dur.config(text=duration)
     prs.config(text='')
     a = len(ets.get())    
     ets.delete(0, a)
     print(start_time)
     print(end_time)
     print(duration)
    
    

def func1(e):  #Enter, 상세정보 변수
     global idx
     global break_u1
     global dlqtl
     
     dlqwhd = time.time()
     tlrks = dlqwhd - dlqtl
     break_u1 = ets.get()    
     a = len(ets.get())    
     ets.delete(0, a)

     break_q = break_korean(Wl[idx])
     break_u = break_korean(break_u1)
     print(f"출제:{break_q}")
     print(f"입력:{break_u}")

     correct = 0
     for c, a in zip(break_q, break_u):
        correct = correct + 1 if c == a else correct
    
     src_len = len(break_q)
     c = correct / src_len * 100
     e = (src_len - correct) / src_len * 100
     speed = float(correct / tlrks) * 60
     
     inf.config(text=f"속도: {speed:0.2f} 정확도: {c:0.2f} % 오타율: {e:0.2f} %")
     print(f"속도: {speed:0.2f} 정확도: {c:0.2f} % 오타율: {e:0.2f} %")

     idx +=1
     prs.config(text=Wl[idx])
    
     dlqtl = 0
     dlqtl = time.time()
    
def break_korean(string):  #한글분리
    break_words = []
    for k in string:
        if ord("가") <= ord(k) <= ord("힣"):
            index = ord(k) - ord("가")
            c_cho = int((index / 28) / 21)
            c_jung = int((index / 28) % 21)
            c_jong = int(index % 28)

            break_words.append(CHO[c_cho])
            break_words.append(JUNG[c_jung])
            if c_jong > 0:
                break_words.append(JONG[c_jong])
        else:
            break_words.append(k)
    return break_words



#tkinter 설정
stb = tk.Button(window, text='시작', command=func2, width=5,height=1)
enb = tk.Button(window, text='종료', command=func3, width=5,height=1)
prsk = tk.Label(window, text='현재 문장 :',)
prs = tk.Label(window, text='', bg='white', width=55, relief='groove', bd=1, anchor='w', fg='black')
inf = tk.Label(window, text='', width=55, bg='white', height=5)
ets = tk.Entry(window, width=55)
plt = tk.Label(window, text='플레이 시간 : ')
dur = tk.Label(window, text='')
ets.bind("<Return>", func1)


prsk.place(x=2, y=200)
prs.place(x=65, y=200)
ets.place(x=65, y=230)
stb.place(x=65, y=260)
enb.place(x=130, y=260)
inf.place(x=65, y=100)
plt.place(x=65, y=60)
dur.place(x=140, y=60)




window.mainloop()