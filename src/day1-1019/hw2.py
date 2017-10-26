# -*- coding: utf-8 -*-
# 2017/10/19(木) 専門ゼミ 第1回 課題
# 2. 変数を5秒間、インクリメントし続け、5秒後にその値を表示する

from __future__ import print_function
import time

start = time.time()     # 計測開始時刻の取得
now = start
cnt = 0                 # インクリメント用変数

# 開始時刻と現在の時間の差が5.0秒未満であればインクリメントし続ける
while now - start < 5.0:
    now = time.time()  # 現在時刻の取得
    cnt += 1
    time.sleep(0.1)         # 0.1秒スリープ

print(cnt)

# 所要時間 : 20分
