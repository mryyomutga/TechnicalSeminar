# -*- coding: utf-8 -*-
# リストについて
l = [1, 22, 333, 45]
print(l)    # リストの中身を表示
print(l[1]) # リストの要素にアクセス

l[2] = 30   # 値を更新
print(l)

# リストの要素数を調べる
print(len(l))

# for文と組み合わせる
points = [88, 76, 67, 43, 79, 80, 91]
sum_v = 0
for i in points:
    sum_v += i
print("合計 :", sum_v)

# sumで合計する
sum_v = sum(points)
print("合計 :", sum_v)

# ランダムにフレーズを表示する
import random

s = ["aaaa","bbbb","cccc","dddd"]
i = random.randint(0, len(s)-1)
print(s[i])

# インデックス付きで
fruits = ["apple", "banana", "orange"]
for i, v in enumerate(fruits):
    print(i, v)

# 要素の追加
a = [1, 2, 3, 4, 5]
a.append(9)
print(a)

# 異なるリストの結合
n1 = [1, 2, 3]
n2 = [2, 3, 4]
n3 = n1 + n2
print(n3)

n1 + = n2
print(n1)

b = [11, 22]
b.extend([33, 44])
print(b)

# 文字列のスライス
a = [i for i in range(0, 10)]
print(a[1:3])
print(a[:4])
print(a[6:])
