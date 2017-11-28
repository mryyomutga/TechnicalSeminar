# -:- coding: utf-8 -*-
# オブジェクト指向について3
class BMI:
    """BMIを計算する"""

    def __init__(self, weight, height):
        """コンストラクタ"""
        self.weight = weight
        self.height = height
        self.calcBMI()

    def calcBMI(self):
        """BMIを計算する"""
        h = self.height / 100
        self.bmi = self.weight / (h ** 2)

    def printJudge(self):
        """結果の表示"""
        print("---")
        print("BMI =", self.bmi)
        b = self.bmi
        if b < 18.5:
            print("痩せ型")
        elif b < 25:
            print("標準")
        elif b < 30:
            print("肥満(軽)")
        else:
            print("肥満(重)")

p1 = BMI(weight = 65, height = 170)
p1.printJudge()

p1 = BMI(weight = 76, height = 165)
p1.printJudge()

p1 = BMI(weight = 50, height = 180)
p1.printJudge()
