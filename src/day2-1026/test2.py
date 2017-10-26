# -*- coding: utf-8 -*-
# リスト内包表記
# 例えば
from __future__ import print_function
import math

l = [10, 20, 30, 40]
print(l)
# リストの要素をルートをとった値に変換したい場合
l[0] = math.sqrt(l[0])
l[1] = math.sqrt(l[1])
l[2] = math.sqrt(l[2])
l[3] = math.sqrt(l[3])
print(l)

# 非常に面倒
l = [10, 20, 30, 40]
print(l)
# これで全部ルートに変換
L = [math.sqrt(x) for x in l]
print(L)
print()

# ユーザー入力を受け付ける
height = float(input("身長を入力してください : ")) / 100
weight = float(input("体重を入力してください : "))

bmi = weight / (height * height)
print("あなたのBMIは {0:0.2f} です".format(bmi))

