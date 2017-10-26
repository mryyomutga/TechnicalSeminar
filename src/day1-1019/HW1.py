# -*- coding: utf-8 -*-
# 2017/10/19(木) 専門ゼミ 第1回 課題
# 1. `(9_9)`と`(6_6)`を0.5秒毎に交互に表示させる

from __future__ import print_function
import time

face = ("(9_9)", "(6_6)")

# 5秒間表示
for n in range(0, 10):
    time.sleep(0.5)
    if n % 2 == 0:
        print(face[0])
    else:
        print(face[1])

# 所要時間 : 3分