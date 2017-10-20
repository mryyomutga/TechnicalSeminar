# -*- coding:utf-8 -*-
# 2017/10/19(木) 専門ゼミ 第1回 課題
# Author : 宮本 涼雅
# Stu.ID : 1536388
# class  : 3EP2-46
# Date : 2017/10/20(金)

from __future__ import print_function
import time

# 1. `(9_9)`と`(6_6)`を0.5秒毎に交互に表示させる

face = ("(9_9)", "(6_6)")

for n in range(0, 10):
    if n % 2 == 0:
        print(face[0])
    else:
        print(face[1])
    time.sleep(0.5)

# 所要時間 : 3分

# 2. 変数を5秒間、インクリメントし続け、5秒後にその値を表示する
# time.time()  現在のUNIX時間の取得

start = time.time() # 計測開始時刻の取得
now_time = start
n = 0               # インクリメント用変数

# 開始時刻と現在の時間の差が5.0秒以下であればインクリメントし続ける
while now_time - start < 5.0:
    now_time = time.time();  # 現在の時刻の取得
    n += 1
    time.sleep(0.1)      # 0.1秒スリープ

print(n)

# 所要時間 : 20分
