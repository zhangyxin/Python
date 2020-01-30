#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/03/28 23:16:01
# @Author  : Jerry
# @File    : ZhuanPanText.py
# @Software: PyCharm

import tkinter
import threading
import time

root = tkinter.Tk()

root.title('英雄联盟')

root.minsize(300, 300)


btn1 = tkinter.Button(root, text='盖伦', bg='red')
btn1.place(x=20, y=20, width=50, height=50)

btn2 = tkinter.Button(root, text='易大师', bg='white')
btn2.place(x=90, y=20, width=50, height=50)

btn3 = tkinter.Button(root, text='瑞文', bg='white')
btn3.place(x=160, y=20, width=50, height=50)

btn4 = tkinter.Button(root, text='维恩', bg='white')
btn4.place(x=230, y=20, width=50, height=50)

btn5 = tkinter.Button(root, text='诺克', bg='white')
btn5.place(x=230, y=90, width=50, height=50)

btn6 = tkinter.Button(root, text='亚索', bg='white')
btn6.place(x=230, y=160, width=50, height=50)

btn7 = tkinter.Button(root, text='安妮', bg='white')
btn7.place(x=230, y=230, width=50, height=50)

btn8 = tkinter.Button(root, text='提莫', bg='white')
btn8.place(x=160, y=230, width=50, height=50)

btn9 = tkinter.Button(root, text='李青', bg='white')
btn9.place(x=90, y=230, width=50, height=50)

btn10 = tkinter.Button(root, text='锤石', bg='white')
btn10.place(x=20, y=230, width=50, height=50)

btn11 = tkinter.Button(root, text='赵信', bg='white')
btn11.place(x=20, y=160, width=50, height=50)

btn12 = tkinter.Button(root, text='瑞兹', bg='white')
btn12.place(x=20, y=90, width=50, height=50)


herolists = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12]

isloop = False
stopsign = False

stopid = None

def round():
    global isloop
    global stopid

    if isloop == True:
        return
    i = 1

    if isinstance(stopid,int):
        i = stopid

    while True:
        time.sleep(0.03)
        for x in herolists:
            x['bg']='white'
        herolists[i]['bg']='red'

        i +=1
        print('当前i为：',i)
        if i>=len(herolists):
            i = 0
        if stopsign == True:
            isloop = False
            stopid = i
            break


def stop1():
    global stopsign

    if stopsign == True:
        return
    stopsign = True
def newtask():
    global isloop
    global stopsign

    stopsign = False
    t = threading.Thread(target=round)
    t.start()
    isloop = True

btn_start = tkinter.Button(root,text="开始",command=newtask)
btn_start.place(x = 90,y=125,width=50,height=50)


btn_stop = tkinter.Button(root,text="停止",command=stop1)
btn_stop.place(x = 160,y=125,width=50,height=50)
root.mainloop()













