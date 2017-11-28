# -*- coding: utf-8 -*-
# オブジェクト指向について2
# コンストラクタ
import math
class CalcFee:
    """計算を行う"""

    # コンストラクタ
    def __init__(self):
        """初期化処理"""
        self.shipping_fee = 1000
        self.tax_rate = 0.08
        self.value = 0

    def addItem(self, price):
        """商品の値段を加算"""
        self.value += price

    def calc(self):
        """料金の計算"""
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        v = math.ceil(total + tax)
        return v

fee1 = CalcFee()
fee1.addItem(500)
print(fee1.calc(), "円")

fee2 = CalcFee()
fee2.addItem(800)
fee2.addItem(500)
print(fee2.calc(), "円")
