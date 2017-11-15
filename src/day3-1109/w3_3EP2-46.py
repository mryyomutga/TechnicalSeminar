# -*- coding: utf-8 -*-
# 2017/11/9(木) 専門ゼミ 第3回 課題
# Author : Ryoga Miyamoto
# コマンドライン上でヒストグラムを表示する
from __future__ import print_function
import random

# 0 ~ 100の整数を1000個生成
points = list(map(lambda x: random.randrange(1, 101), [n for n in range(1000)]))
hist = [0] * 11

# 生成された乱数から階級毎の度数を記録
for n in points:
    if 0 <= n < 10:
        hist[0] += 1
    elif 10 <= n < 20:
        hist[1] += 1
    elif 20 <= n < 30:
        hist[2] += 1
    elif 30 <= n < 40:
        hist[3] += 1
    elif 40 <= n < 50:
        hist[4] += 1
    elif 50 <= n < 60:
        hist[5] += 1
    elif 60 <= n < 70:
        hist[6] += 1
    elif 70 <= n < 80:
        hist[7] += 1
    elif 80 <= n < 90:
        hist[8] += 1
    elif 90 <= n < 100:
        hist[9] += 1
    elif n == 100:
        hist[10] += 1

# 度数の表示
for i, n in enumerate(hist):
    v = int(n / 10) + 1
    # 文字列のフォーマット
    s1 = "|" * v
    s = "{0}1 ~ {0}9 [{1:>3}] : {2}".format(i, n, s1)
    if i == 0:
        s = " 1 ~  9 [{1:>3}] : {2}".format(i, n, s1)
    elif i == len(hist) - 1:
        s = "   100  [{1:>3}] : {2}".format(i, n, s1)

    print(s)
