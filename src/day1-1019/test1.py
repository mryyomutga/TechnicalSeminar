# -*- coding:utf-8 -*-
# Python3のprintを使えるようにする
from __future__ import print_function

# 三角関数を使えるように機能拡張する
import math

x = 0.4
math.sin(x)
math.cos(x)
math.pi
math.e

dir(math)
help(math)

L=[123, 10]	# リスト
len(L)		# 要素数の取得
L.append("1232131")	# リストに要素を追加する

L.remove(123)	# 指定したものが含まれる場合，それを削除
del L[1]	# インデックスを指定して削除

L=(10, 20, 30)	#タプル
# 要素の変更ができないリストのようなもの

#range(start,end)
# startからend-1までのリストを作成

#range(start,end,step)
# startからend-1までstepごとにリストを作成

x=range(100, 50, -5)
# inを使えばリストやタプルにそれが入っているか確認できる
55 in x
56 in x

# 型を調べる
isinstance(x, type)	# True/False
type(x)				# 型を表示

dir()	# 使用した変数を表示

# 見やすく整形する
from pprint import pprint
pprint(dir())

# 関数の定義
# ブロックはインデントで行う

def sum(x, y):
	print(a)
	print(b)
	return a + b

sum(100,200)


