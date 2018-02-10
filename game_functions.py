#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/10

import sys
import pygame

def check_events():
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()