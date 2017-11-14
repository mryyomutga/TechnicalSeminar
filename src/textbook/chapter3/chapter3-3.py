# -*- coding: utf-8 -*-
# 文字列
s1 = "Hello. I'm a student."
# 三重引用符での文字列の生成
s2 = """\
三重引用符での文字列生成"""
print(s1)
print(s2)

# 数値から文字列に変換する
n = 12345
print(str(n))

# 文字列に対する演算
s1 = "abc"
s2 = "def"
print(s1 + s2)
print(s1 * 3)

# 文字列の抽出
s = "abcd"
print(s[0], s[2])

# 文字列のスライス
s = "abcdefghijklmn"
print(s[1:4])   # リストのようにスライスする

# 文字列の分割
# split(文字, maxsplit)
s = "This is a pen."
print(s.split())
# /で1回だけ区切る
s = "2017/11/14"
print(s.split("/", maxsplit=1))

# 文字列の結合
day = s.split("/")
print("-".join(day))

# 文字列の置換
# str.replace(old, new [,count])
s = "This is a pen."
print(s.replace("pen", "notebook"))
print(s)
