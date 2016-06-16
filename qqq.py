#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet
from pyglet.gl import *
  
def on_resize(width, height):
    glViewport(0, 0, width, height)#當視窗長寬改變時，畫面也跟著變 
    glMatrixMode(GL_PROJECTION)#投影矩陣模式  
    glLoadIdentity()#將OpenGL中的矩陣設為單位矩陣  不希望之前的矩陣資料殘留到現在的運算 
    gluPerspective(50., width / float(height), 1., 100.)#視角 高寬比 距離(進) 距離(遠)
    glMatrixMode(GL_MODELVIEW)#改成模型矩陣 做旋轉、平移、縮放 
  
def setup():
    glClearColor(1, 1, 1, 1)#設定用來清理顏色緩衝區的顏色，避免畫面殘留  紅 , 綠 , 藍 , 透明色
    glColor3f(.5, .5, .5)
  
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)#真正動手清理緩衝區 
    glLoadIdentity()
    glTranslatef(0, 0, -5)#立體模型的平移 x y z
    glRotatef(r, 0, 0, 1)#以Z軸當旋轉軸
    glRectf(1, 1, -1, -1)#矩形
  
r = 0
def update(dt):#秒數
    global r
    r += 1
    if r > 360:
        r = 0
pyglet.clock.schedule_interval(update, 1/20.0)
  
w1 = pyglet.window.Window(200, 200, caption='First window')#調整你的窗口
w1.on_resize = on_resize
w1.on_draw = on_draw
w1.switch_to()#將GL放入窗口(如果只有一個窗口就不用)
#setup()
  
w2 = pyglet.window.Window(300, 300, caption='Second window', resizable=True)
w2.on_resize = on_resize
w2.on_draw = on_draw
w2.switch_to()
setup()
  
pyglet.app.run()