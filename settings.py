#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/10

class Settings():
    #存储《外星人入侵》的所有设置的类
    
    def __init__(self):
        #初始化游戏的设置
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #飞船速度
        self.ship_speed_factor = 1
        
        #子弹设置
        self.bullet_speed_factor = 0.1
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 255,0,0