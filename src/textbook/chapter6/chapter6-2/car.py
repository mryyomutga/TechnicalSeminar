# -*- coding: utf-8 -*-
# クラスの継承
# 基底クラス
class Car:
    """自動車クラス"""
    def __init__(self, owner):
        """コンストラクタ"""
        self.handle = 0
        self.car_type = "normal"
        self.owner = owner

    def turn_left(self):
        """ハンドルを左に切る"""
        self.handle -= 90

    def turn_right(self):
        """ハンドルを右に切る"""
        self.handle += 90

    def show_status(self):
        """状態の表示"""
        print("-----")
        print("owner :", self.owner)
        print("car_type :", self.car_type)
        print("handle :", self.handle)

# 派生クラス
class Van(Car):
    """ワゴン車クラス"""
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "Van"

    def open_door(self):
        """ドアを開く"""
        print("ドアを開けました")

    def close_door(self):
        """ドアを閉じる"""
        print("ドアを閉じました")

class Camper(Car):
    """キャンピングカークラス"""
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "camper"

    def make_ice(self):
        """製氷する"""
        print("氷を作りました")
