# -*- coding: utf-8 -*-
# 2017/11/9(木)
# Author : Ryoga Miyamoto
from __future__ import print_function
import random

# 0 ~ 100の整数を1000個生成
points = list(map(lambda x: random.randrange(1, 101), [n for n in range(1000)]))
hist = [0] * 11

# 生成された乱数から階級毎の度数を記録
for n in points:
    r = int(n / 10)
    hist[r] += 1

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
