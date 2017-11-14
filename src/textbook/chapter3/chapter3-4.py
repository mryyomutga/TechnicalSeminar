# -*- coding: utf-8 -*-
# 関数
# def name(arg):
def mul(a, b):
    return a * b

print(mul(2, 3))

# docstringを付ける
def mul(a, b):
    """掛け算を行う"""
    return a * b

# docstringの確認
help(mul)

# 再帰呼び出し
def say(i):
    if i <= 0:
        return
    print(i, "Hello!")
    # 自身を呼び出す
    say(i - 1)

say(5)

# デフォルト引数
def say(mes = "Hello"):
    print(mes)
say()   # Hello
say("Good bye") # Good bye

# 名前付き引数
def calc_time(dist, speed):
    t = dist / speed
    return round(t, 1)
# 呼び出すときに引数名を指定
print(calc_time(dist=1000, speed=230))

# 可変長引数
def sum_args(*args):
    v = 0
    for n in args:
        v += n
    return v
print(sum_args(1))
print(sum_args(1, 2, 3, 4, 5))

# 辞書型の可変長引数
def print_arg(**args):
    print(args)
print_arg(A="a", B="b", C="c")
print_arg(n1=23, n2=34, n3=45, n4=56)

# ローカル変数とグローバル変数
value = 100
def change_value():
    value = 20
# change_valueの変数valueを変更している
change_value()
# 関数外には影響を与えない
print(value)

def change_value():
    global value
    value = 20
change_value()
print(value)
