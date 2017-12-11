# -*- coding: utf-8 -*-
# 特殊メソッド

class Pos:
    """座標クラス"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+演算子の動作
        新しいインスタンスを返す"""
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __str__(self):
        """文字列として取得する際の動作"""
        return "({0}, {1})".format(self.x, self.y)

p1 = Pos(10, 20)
p2 = Pos(30, 40)

# インスタンスの演算
p3 = p1 + p2
print(p3)
