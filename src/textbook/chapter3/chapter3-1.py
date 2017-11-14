# -*- coding: utf-8 -*-
# リスト
a = [1, 2, 3, 4]
print(a)

# 要素にアクセス
print(a[2])
# 値の更新
a[0] = 0
print(a)

# 要素数の取得
print(len(a))

# for文と組み合わせる
for i in a:
    print(i)

# sumでリストの値を合計する
print(sum(a))

# インデックス付きで繰り返す
for i,v in enumerate(a):
    print(i, v)

# 要素の追加
num = [0, 1, 2]
num.append(3)
print(num)

# 2つのリストを結合する
a = [0, 1, 2]
b = [1, 2, 3]
c = a + b
print(c)

# リストに異なるリストの要素を追加する
a += b
print(a)

# extendで追加する
b.extend([4, 5, 6])
print(b)

# リストをスライス
num = [i for i in range(10)]
# 指定範囲で切り出す
print(num[1:4])
# 先頭から指定番号まで切り出す
print(num[:5])
# 指定番号から末尾まで切り出す
print(num[6:])
# 末尾からインデックスを指定する
print(num[-2])
# step毎に取り出す
print(num[0:8:2])

# 要素の削除
del num[2]
print(num)
# スライスを指定して削除する
num = [i for i in range(10)]
del num[2:4]

# タプル
# 内容を更新できない
a = (0, 1, 2)
print(a[0])
print(a[:2])

# 集合型(set)
# 重複・順序をつけることができない
color = {"red", "green", "blue"}
print(color)

# 空のsetを作成する
e = set()
print(e)


# 数学的な演算を行う
box1 = {"ハンマー", "釘", " ペンチ"}
box2 = {"釘", " ペンチ"}
# 差分
print(box1 - box2)

# 1つにまとめる
t1 = {1, 2, 3, 4}
t2 = {4, 7, 8, 9}
print(t1 | t2)

# 共通部分を抜き出す
print(t1 & t2)
