# -*- coding: utf-8 -*-
# 特殊メソッド2

class Pos:
    """座標クラス"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Pos(self.x * other, self.y * other)
        else:
            raise TypeError

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = Pos(10, 20)
p2 = p1 * 1.7
print(p2)
