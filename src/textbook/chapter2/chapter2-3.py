# -*- coding: utf-8 -*-
# 文字列
# エスケープシーケンス
print("I can\'t speak English.")

# 三重引用符

mes = """\
先頭と末尾に
バックスラッシュを入れると
出力時に1行目と末尾に
改行が入らなくなる\
"""
print(mes)

# 文字列の連結
s = "Hello," + "World!"
print(s)
s1 = "Hello,"
s2 = "World!"
print(s1 + s2)

# 文字列に変数を埋め込む
temp = 28
print("現在の気温は" + str(temp) + "度です")

# formatで値を埋め込む
per_inch = 2.54
inch = 24
cm = inch * per_inch
desc = "{0} inch = {1} cm".format(inch, cm)
print(desc)

# 名前付きのformat
print(
    "My name is {name}. I am {age} years old. I am {job}."
    .format(name="Bob", age=24, job="Programer")
    )
