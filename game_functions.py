#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/10

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建子弹，并假如到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
        
def fire_bullet(ai_settings,screen,ship,bullets):
    new_bullet = Bullet(ai_settings,screen,ship)
    bullets.add(new_bullet)

        
def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship) 
           

def update_screen(ai_settings,screen,ship,bullets):
    #更新屏幕上的图像，切换到新屏幕
    #每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    
    #在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()