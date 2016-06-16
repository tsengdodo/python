#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet  
import random  
  
from pyglet.window import key   
from pyglet.window import mouse  
  
  
game_window=pyglet.window.Window(1200,700)  
t=0  
lable=pyglet.text.Label('Come On Baby',font_name='Times New Roman',font_size=36,x=game_window.width/2
    ,y=game_window.height/2,anchor_x='center',anchor_y='center')    
image_s=pyglet.image.load('n.png')  
image_dabian=pyglet.image.load('h.png')  
  

man=pyglet.sprite.Sprite(img=image_s,x=500,y=0);#顯示位置 初始化遊戲主角  
  
keys = key.KeyStateHandler()  #獲取按键狀態 
game_window.push_handlers(keys)  #按鍵
  
dabian_lives=[]  
for i in range(5):  
    rand_x=random.randrange(0,1200,1)  
  
    new_sprite=pyglet.sprite.Sprite(img=image_dabian,x=rand_x,y=700)  #顯示位置
    new_sprite.scale=0.3   #咚咚的大小
    dabian_lives.append(new_sprite)  
      
  #咚咚範圍
def check_bounds(self):  
    if self.y<-100:  
        rand_x=random.randrange(-200,200,10)    
        self.x+=rand_x  
        if self.x<0:  
            self.x=0  
        elif self.x>1200:  
            self.x=1200      
        self.y=700  
 
@game_window.event   #讓窗口知道這個事件
def on_draw():  
    game_window.clear()  
    lable.draw()   #視窗
    man.draw()     #主角
    for live in dabian_lives:  #掉落的
        live.draw()  
     
@game_window.event  
def on_mouse_press(x,y,button,modif):  
    if button==mouse.LEFT:  
        print'mouse left was pressed!'  
  
    elif button==mouse.RIGHT:  
        print'mouse right was pressed!'  
    print x  
    print y  

#主角能跑的範圍   
def update(dt):  
    if keys[key.LEFT]:  
        man.x-=10  
    elif keys[key.RIGHT]:  
        man.x+=10     
    elif keys[key.UP]:  
        man.y+=10  
    elif keys[key.DOWN]:  
        man.y-=10   
    if man.y>300:  
        man.y=300  
    elif man.y<-300:  
        man.y=-300 
      
    if man.x>1000:  
        man.x=1000  
    elif man.x<0:  
        man.x=0      
    for live in dabian_lives:  
        rand_y=random.randrange(100)  #咚咚往下掉的速度
        live.y-=rand_y  
        
        check_bounds(live)  #看有沒有出借
        
    
pyglet.clock.schedule_interval(update, 1/100.0)  

       
pyglet.app.run()  