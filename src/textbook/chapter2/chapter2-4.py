# -*- coding: utf-8 -*-
# ユーザー入力の受付

name = input("あなたの名前は? ")
print(name + "さん、こんにちは。")

# inch -> cm
per_inch = 2.54
# 入力された値は文字列型になる
inch = float(input("inch? "))
cm = inch * per_inch
print("{0} inch = {1} cm".format(inch, cm))

# 変数の型を調べる
print(type(30))
print(type(3.1415))
print(type("abc"))
