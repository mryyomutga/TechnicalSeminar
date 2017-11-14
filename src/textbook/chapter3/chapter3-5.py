# -*- coding: utf-8 -*-
# 無名関数(lambda式)
# 関数オブジェクト
def mul_func(a, b):
    return a * b
# 関数オブジェクトの生成
func = mul_func
print(func(2, 5))

# 関数の引数に関数を指定する
def add_func(args):
    val = 0
    for n in args:
        val += n
    return val
def mul_func(args):
    val = 1
    for n in args:
        val *= n
    return val

# 引数に関数を要求
def calculate(func, args):
    return func(args)

values = [n for n in range(1, 11)]
# 関数オブジェクトを関数に渡す
result = calculate(add_func, values)
print(result)
result = calculate(mul_func, values)
print(result)

# lambda式
# lambda式の返り値は関数オブジェクト
# lambda args : statement
tri = lambda a, b: a * b / 2
print(tri(12, 3))

def calculate(func, a, b):
    return func(a, b)
# lambda式で簡潔に記述
result = calculate(lambda a, b: a * b, 5, 3)

# lambda式とmapを組み合わせる
# 1~10の数値リストをすべて2倍してリスト化
print(list(map(lambda x: x * 2, [n for n in range(1, 11)])))

# lambda式とfilterを組み合わせる
# 1~10の数値リストから偶数を抽出してリスト化
print(list(filter(lambda x: x % 2 == 0, [n for n in range(1, 11)])))

# タプルのリストをソートする
animals = [("ライオン", 58),
           ("チーター", 110),
           ("シマウマ", 60),
           ("トナカイ", 80)
           ]
faster = sorted(animals, key=lambda ani: ani[1], reverse=True)
for i in faster:
    print(i)

# 辞書をソートする
animals = {"ライオン":58,
           "チーター":110,
           "シマウマ":60,
           "トナカイ":80
           }
# items()で辞書型をタプルのリストに変換する
faster = sorted(animals.items(), key=lambda x: x[1], reverse=True)
for key, val in faster:
    print(key, val)
