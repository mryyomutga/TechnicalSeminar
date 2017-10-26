#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
import random
 
pygame.init()
 
# 色の定義
black = [  0,  0,  0]
white = [255,255,255]
 
# スクリーンの設定
size=[1000,500]
screen=pygame.display.set_mode(size)
 
# キャプションの設定
pygame.display.set_caption("Bouncing Rectangle")
 
# ゲームループ制御フラグ
done=False
 
# クロック制御オブジェクト
clock = pygame.time.Clock()
 
 
# 雪の初期位置
star_list = []
for i in range(100):
    x = random.randrange(0,size[0])
    y = random.randrange(0,size[1])
    star_list.append([x,y])
 
# ゲームループ
col=white
while done==False:
    # イベント制御
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT:
            done=True
        if ev.type == pygame.KEYDOWN:
            if ev.key  == pygame.K_w:
                col=white
            else:
                col=[random.randrange(0,255) for _ in range(0,3)]
                
    # 背景の描画
    screen.fill(black)
   
    # 雪のアニメーション
    for item in star_list:
        item[1] += 2
        item[0] += random.randrange(-1,2)
        # 雪の描画
        pygame.draw.circle(screen,col,item,10)
 
        # 画面外に出たら画面上のランダムな位置に戻す
        if item[1] > size[1]:
            item[1] = random.randrange(-20,-5)
            item[0] = random.randrange(size[0])
 
 
    # 描画の実行
    pygame.display.flip()
 
    # フレームレートの設定
    clock.tick(30)
 
# ゲーム終了
pygame.quit()
